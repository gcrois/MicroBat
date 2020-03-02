# This file holds the URLs and what logic each should do.
from flask import render_template, flash, redirect
from app import app
from app.forms import JoinSessionForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
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
    return render_template('base.html', title = 'Home', header = header)

# Page for the hosting device.
@app.route('/host')
def host():
    header = "Hosting page for Microbat"

    # This function is cool. Research it.
    return render_template('base.html', title = 'Host', header = header)

# For users.
# Must be logged in to veiw. That's what the second decorator does.
@app.route('/user')
@login_required
def users():
    # Temporary user. We can change this dynamically.
    user = current_user.name
    header = "User: " + user

    # This function is cool. Research it.
    return render_template('base.html', title = 'user', header = header)

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
        # If the user isn't in the table, or they entered the wrong pass
        if user is None or not user.decode_password(form.password.data):
            # This is Flask stuff. It just 'flashes' a message to the user.
            flash('Invalid username or password!')
            return redirect('/join')
        login_user(user)
        return redirect('/user')

    return render_template('join.html', title = 'Join Session', header = header, form = form)

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/home')
