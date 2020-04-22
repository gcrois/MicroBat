# This file holds the URLs and the logic for each.
from flask import render_template, flash, redirect, url_for
from app import app
from app import dataBase as db
from app.forms import HostForm, PollForm, RegisterForm, JoinSessionForm, \
                      ResponseForm, DataForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Session, Poll

# The '@' symbol demarks a 'decorator'
# They simply modify a function in a desirable way.
# These simply tell the functions that follow them to
# execute when the url specified in the .routes() function
# is evoked.

# Right now it returns a neat function you should research.
# Essentially we can define templated HTML(and CSS) that Flask
# will change dynamically for us. Check the arguments I've passed
# in and look at app/templates/temp.html
@app.route('/')
@app.route('/home')
def home():
    # This function is cool. Research it.
    return render_template('home.html', title='Home')

# Page for the hosting device.
@app.route('/host', methods=['GET', 'POST'])
def host():
    header = "Hosting page for Microbat"
    
    form = HostForm()

    if form.validate_on_submit():
        if form.poll.data:
            return redirect(url_for('hostPoll'))
        if form.greg.data:
            return redirect(url_for('greg'))
        if form.BlackJack.data:
            return redirect(url_for('blackjack'))


    # This function is cool. Research it.
    return render_template('host.html', title='Host', header=header, form=form)

# This is the route for hosting a poll
@app.route('/host_poll', methods=['GET', 'POST'])
def hostPoll():
    header = "Enter your desired poll!"

    form = PollForm()

    print("We're in host poll")

    if form.validate_on_submit():
        # We need to create the session and the poll, then link them
        # together.
        print("Form submitted")
        sesh = Session(session_id = form.sessionID.data)
        poll = Poll(question = form.questionText.data)

        session = Session.query.filter_by(session_id = form.sessionID.data).first()

        # If the session doesn't exist
        if not (session is None):
            flash('Session in use!')
            return redirect('/host_poll')

        poll.a = form.a.data
        poll.b = form.b.data
        poll.c = form.c.data
        poll.d = form.d.data

        poll.a_num = 0
        poll.b_num = 0
        poll.c_num = 0
        poll.d_num = 0

        # Link them
        poll.session = sesh
        sesh.poll = poll

        db.session.add(sesh)
        db.session.commit()

        db.session.add(poll)
        db.session.commit()

        flash("Generating poll!")
        return redirect('/pollData/'+sesh.session_id)

    return render_template('create_poll.html', title='Host a Poll', header=header, form=form)

@app.route('/pollData/<sesh_id>', methods=["GET", "POST"])
def pollData(sesh_id):
    header = "Polling Data"
    form = DataForm()

    sesh = Session.query.filter_by(session_id=sesh_id).first()
    poll = sesh.poll

    question = poll.question

    total_count = poll.a_num + poll.b_num + poll.c_num + poll.d_num

    a_perc = 0
    b_perc = 0
    c_perc = 0
    d_perc = 0

    print(poll.a_num)

    if poll.a_num > 0:
        a_perc = round((poll.a_num / total_count)*100, 2)
    if poll.b_num > 0:
        b_perc = round((poll.b_num / total_count)*100, 2)
    if poll.c_num > 0:
        c_perc = round((poll.c_num / total_count)*100, 2)
    if poll.d_num > 0:
        d_perc = round((poll.d_num / total_count)*100, 2)

    data = [
        (poll.a, a_perc),
        (poll.b, b_perc),
        (poll.c, c_perc),
        (poll.d, d_perc)
    ]

    if form.validate_on_submit():
        # To close the poll we need to end the session and delete the poll from
        # the database.
        if form.close.data:

            db.session.delete(poll)
            db.session.commit()
            db.session.delete(sesh)
            db.session.commit()

            flash("Polling closed! Thanks for hosting your poll!")
            return redirect('/home')
        else:
            return redirect('/pollData/'+sesh.session_id)


    return render_template('data.html', title='Data', header=header,
                           question=question, data=data, form=form)


# These are the routes for your guy's stuff.
@app.route('/greg')
def greg():
    header = "Greg's Thing."

    return render_template('base.html', title='Greg', header=header)

#BlackJack Player view
@app.route('/blackjack')
def blackjack():

    return render_template('blackjack_player.html')


# For users.
# Must be logged in to veiw. That's what the second decorator does.
@app.route('/user/<username>/<session_id>', methods=['GET', 'POST'])
@login_required
def users(username, session_id):
    # Temporary user. We can change this dynamically.
    user = User.query.filter_by(name=username).first_or_404()
    session = Session.query.filter_by(session_id = session_id).first_or_404()
    poll = session.poll

    header = "User: " + user.name + " -- Session: " + session.session_id
    form = ResponseForm()

    # When someone's submitted a response.
    if form.validate_on_submit():
        flag = False

        if form.a.data:
            poll.a_num+=1
            flag = True

        if form.b.data:
            poll.b_num+=1
            flag = True

        if form.c.data:
            poll.c_num+=1
            flag = True

        if form.d.data:
            poll.d_num+=1
            flag = True

        if flag:
            db.session.commit()
            flash("Response logged. Thanks!")
            return redirect('/home')
        else:
            flash("Please select atleast one response!")

    # Pull the poll from the DB object.
    question = poll.question

    answers = [poll.a, poll.b, poll.c, poll.d]

    # This function is cool. Research it.
    return render_template('response.html',
           title='user', header=header, question=question,
           answers=answers, form=form)

# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is already logged in and they try to go back to login
    # We just send them on their way.
    if current_user.is_authenticated:
        return redirect('/user')

    form = RegisterForm()
    header = 'Register'

    if form.validate_on_submit():
        # Here we're building a new User object and
        # adding them to our database
        user = User(name = form.user.data)
        user.hash_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Yay! You're registered!")
        return redirect('/join')

    return render_template('register.html', title='Register2', header=header, form=form)

# Login. We user a lot of cool libraries and extensions for this.
@app.route('/join', methods=['GET', 'POST'])
def join():

    form = JoinSessionForm()
    header = 'Join Session Page'

    # More wtform stuff. Just read the docs.
    if form.validate_on_submit():

        user = User.query.filter_by(name=form.user.data).first()
        session = Session.query.filter_by(session_id = form.sessionID.data).first()

        # If the user isn't in the table, or they entered the wrong pass
        if user is None or not user.decode_password(form.password.data):
            # This is Flask stuff. It just 'flashes' a message to the user.
            flash('Invalid username or password!')
            return redirect('/join')

        # If the session doesn't exist
        if session is None:
            flash('Invalid Session!')
            return redirect('/join')

        # Log the user in and add them to the session.
        login_user(user)
        user.session = session

        return redirect('/user/'+user.name+'/'+session.session_id)

    return render_template('join.html', title='Join Session', header=header, form=form)

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/home')
