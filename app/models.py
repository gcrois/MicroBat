# This file houses our DataBase objects.
# Right now we're working with SQLite, so no server.
# This is cool for development, and SQLAlchemy will allow us to
# port over to MYSQL eventually if we want to take it live.

# We're using SQLALCHEMY ORM if you want to read the docs.

from app import dataBase as db

class User(db.Model):
    # Primary Key means this is a unique value - Meaning all
    # users in our database will be assigned a unique ID.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    session = db.Column(db.Integer, index=True)
    passHash = db.Column(db.String(128))
    # Each user is going to have some number of answers
    # associated with them. This line links the user table to the answer table
    # to facilitate this.

    # Google 'Flask-SQLAlchemy One to Many' for info.
    # The short and sweet is we can now call user.answers and get a list of answers.
    # backref allows us to call answer.user to return the user who gave that answer.
    answers = db.relationship('Answer', backref='user', lazy=True)

    # This is just a debugging helper.
    # It just tells python's print() method how
    # to print a User object

    def __repr__(self):
        return 'User: {}'.format(self.name) + ' Session: {}'.format(self.session)

# Right now an answer is simply a string limited to 140 characters.
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ans = db.Column(db.String(140))
    # ForeignKey tells SQLAlchemy to reference the user table the id.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Answer: {}'.format(self.ans)
