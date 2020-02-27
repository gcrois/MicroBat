# This is where our imports go.
from flask import Flask
# These are the configurations we need for flask.
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 'routes' are our urls.
# We need to implement them using 'decorators'.
# That'll become apparent in the server file.
from app import routes
