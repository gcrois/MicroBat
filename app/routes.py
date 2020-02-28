# This file holds the URLs and what logic each should do.
from flask import render_template, flash, redirect
from app import app
from app.forms import JoinSessionForm

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
@app.route('/user')
def users():
    # Temporary user. We can change this dynamically.
    user = "The Big J "
    header = "User: " + user

    # This function is cool. Research it.
    return render_template('base.html', title = 'user', header = header)

# Login
@app.route('/join', methods=['GET', 'POST'])
def join():
    form = JoinSessionForm()
    header = 'Join Session Page'

    # More wtform stuff. Just read the docs.
    if form.validate_on_submit():
        # This is Flask stuff. It just 'flashes' a message to the user.
        flash('User: "{}" joined session: {}'.format(form.user.data, form.sessionID.data))
        return redirect('/user')

    return render_template('join.html', title = 'Join Session', header = header, form = form)
