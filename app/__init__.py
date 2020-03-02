# This is where our imports go.
from flask import Flask
# These are the configurations we need for flask and SQLite
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
# This is how we manage user login
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
# This tells the login object the veiw function that logs users in.
login.login_view = 'join'

# Here's our database
dataBase = SQLAlchemy(app)
engine = create_engine('sqlite:///app.db', echo = True)

# 'routes' are our urls.
# We need to implement them using 'decorators'.
# That'll become apparent in the server file.

# Models are the classes associated with our database.
# This is from SQLAlchemy. It allows us to work with databases
# with higher-level abstraction like functions and classes
# instead of SQL.
from app import routes, models
