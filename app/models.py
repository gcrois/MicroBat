# This file houses our DataBase objects.
# Right now we're working with SQLite, so no server.
# This is cool for development, and SQLAlchemy will allow us to
# port over to MYSQL eventually if we want to take it live.

# We're using SQLALCHEMY ORM if you want to read the docs.

from app import dataBase as db, login
# This allows us to generate and authenticate a hashable password
from werkzeug.security import check_password_hash, generate_password_hash

# This is a no fuss base model that does everything flask_login wants without
# ruining everything else.
from flask_login import UserMixin

# We're about to use our database for the very first time guys.
# *wipes away tear*

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), index=True, unique=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))

    users = db.relationship('User', backref='session', lazy=True)
    poll = db.relationship("Poll", uselist=False, back_populates='session')

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    session = db.relationship("Session", uselist=False, back_populates='poll')

    # responses
    a = db.Column(db.String(140))
    b = db.Column(db.String(140))
    c = db.Column(db.String(140))
    d = db.Column(db.String(140))

    # Number of responses per response
    a_num = db.Column(db.Integer)
    b_num = db.Column(db.Integer)
    c_num = db.Column(db.Integer)
    d_num = db.Column(db.Integer) 

class User(UserMixin, db.Model):
    # Primary Key means this is a unique value - Meaning all
    # users in our database will be assigned a unique ID.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=True)
    passHash = db.Column(db.String(128))
    # Each user is going to have some number of answers
    # associated with them. This line links the user table to the answer table
    # to facilitate this.

    # Google 'Flask-SQLAlchemy One to Many' for info.
    # The short and sweet is we can now call user.answers and get a list of answers.
    # backref allows us to call answer.user to return the user who gave that answer.
    answers = db.relationship('Answer', backref='user', lazy=True)

    # Password processing
    def hash_password(self, password):
        self.passHash = generate_password_hash(password)

    def decode_password(self, password):
        return check_password_hash(self.passHash, password)

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

db.create_all()
