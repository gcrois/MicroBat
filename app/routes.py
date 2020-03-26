# This file holds the URLs and what logic each should do.
from flask import render_template, flash, redirect, url_for
from app import app
from app import dataBase as db
from app.forms import HostForm, PollForm, RegisterForm, JoinSessionForm
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
    header = "Homepage for Microbat"
    # This function is cool. Research it.
    return render_template('base.html', title='Home', header=header)

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
        if form.tim.data:
            return redirect(url_for('tim'))


    # This function is cool. Research it.
    return render_template('host.html', title='Host', header=header, form=form)

# This is the route for hosting a poll
@app.route('/host_poll', methods=['GET', 'POST'])
def hostPoll():
    header = "Enter your desired poll!"

    form = PollForm()

    return render_template('create_poll.html', title='Host a Poll', header=header, form=form)

# These are the routes for your guy's stuff.
@app.route('/greg')
def greg():
    header = "Greg's Thing."

    return render_template('base.html', title='Greg', header=header)

@app.route('/tim')
def tim():
    header = "Tim's thing."

    return render_template('base.html', title='Tim', header=header)


# For users.
# Must be logged in to veiw. That's what the second decorator does.
@app.route('/user')
@login_required
def users():
    # Temporary user. We can change this dynamically.
    user = current_user.name
    header = "User: " + user

    # This function is cool. Research it.
    return render_template('base.html', title='user', header=header)

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
    # If the user is already logged in and they try to go back to login
    # We just send them on their way.
    if current_user.is_authenticated:
        return redirect('/user')

    form = JoinSessionForm()
    header = 'Join Session Page'

    # More wtform stuff. Just read the docs.
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.user.data).first()
        session = Session.query.filter_by(session_id = form.session.ID.data)
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
        
        return redirect('/user')

    return render_template('join.html', title='Join Session', header=header, form=form)

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/home')
