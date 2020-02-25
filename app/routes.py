# This file holds the URLs and what logic each should do.

from app import app

# The '@' symbol demarks a 'decorator'
# They simply modify a function in a desirable way.
# These simply tell the functions that follow them to
# execute when the url specified in the .routes() function
# is evoked.

# Right now this just creates a very simple html page.
@app.route('/')
@app.route('/home')
def home():
    return '''
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Home Page for 'insert catchy project title here.'</h1>
        <h2>We need to figure out if we're doing this all in HTML or JS and CSS too.</h2>
    </body>
</html>'''

# Generic webpage for all users.
# no clue how we'd make a dynamic page for an ambiguous user.
@app.route('/users')
def users():
    return '''
<html>
    <head>
        <title>USER</title>
    </head>
    <body>
        <h1>This is the webpage participants will see.</h1>
        <h1>It needs to be ambigous so we can create it dynamically for each user.</h1>
    </body>
</html>'''
