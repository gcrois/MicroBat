# This file holds the URLs and what logic each should do.
from flask import render_template
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
@app.route('/host')
def home():
    header = "Homepage for cool project name"

    # This function is cool. Research it.
    return render_template('base.html', title = 'Host', header = header)

# For users.
@app.route('/user')
def users():
    # Temporary user. We can change this dynamically.
    user = "The Big J"
    header = "User: " + user + '.'

    # This function is cool. Research it.
    return render_template('base.html', title = 'user', header = header)

@app.route('/')
@app.route('/join')
def join():
    form = JoinSessionForm()
    header = 'Join Session Page'
    return render_template('join.html', title = 'Join Session', header = header, form = form)
