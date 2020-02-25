# This file holds the URLs and what logic each should do.

from app import app

# The '@' symbol demarks a 'decorator'
# They simply modify a function in a desirable way.
# These simply tell the functions that follow them to
# execute when the url specified in the .routes() function
# is evoked.

@app.route('/')
@app.route('/home')
def home():
    message = "This is the homepage for 'insert catchy project title here'"
    return message

@app.route('/users')
def users():
    return "This page is for users."
