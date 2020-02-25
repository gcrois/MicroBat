# This file holds the URLs and what logic each should do.
from flask import render_template
from app import app

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
    text = "Homepage for cool project name"
    # This function is cool. Research it.
    return render_template('temp.html', title = 'User', text=text)

# For users.
@app.route('/users')
def users():
    # Temporary user. We can change this dynamically.
    user = "The Big J"
    text = "User: " + user + '.'

    # This function is cool. Research it.
    return render_template('temp.html', title = 'User', text=text)
