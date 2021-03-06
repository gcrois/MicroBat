# All this file does is give us access to a flask shell. 

from app import app, dataBase
from app.models import User, Answer, Session, Poll


# This allows us to open up a Python shell for testing
# without having to do all those silly flask imports first.
# simply type "flask shell" in the command line.

@app.shell_context_processor
def make_shell_context():
    return{'db': dataBase, 'User': User, 'Answer': Answer, 'Poll': Poll, 'Session' : Session}
