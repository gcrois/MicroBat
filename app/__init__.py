# This is where our imports go.

from flask import Flask

app = Flask(__name__)

# 'routes' are our urls.
# We need to implement them using 'decorators'.
# That'll become apparent in the server file.
from app import routes
