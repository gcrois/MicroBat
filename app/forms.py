# This is where we store web forms.
# Things like the join session form for users.
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, \
SubmitField, BooleanField, FieldList, FormField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class HostForm(FlaskForm):
    ''' This is how hosts select the thing they want to host. '''

    poll = SubmitField('Host a Poll')
    greg = SubmitField('Gregs thing')
    CreateBlackJack = SubmitField('BlackJack')

####  These are the forms for the polling app ####
class PollForm(FlaskForm):
    ''' Webform for creating a poll. '''
    sessionID = IntegerField('Session ID (Numeric)', validators=[DataRequired()])
    questionText = StringField('Question', validators=[DataRequired()])
    submit = SubmitField('Post poll')

    a = StringField('Response A', validators=[DataRequired()])
    b = StringField('Response B', validators=[DataRequired()])
    c = StringField('Response C', validators=[DataRequired()])
    d = StringField('Response D', validators=[DataRequired()])

class ResponseForm(FlaskForm):
    ''' Webform for recieving answers from users '''

    a = BooleanField()
    b = BooleanField()
    c = BooleanField()
    d = BooleanField()

    submit = SubmitField('Submit Response(s)')

class DataForm(FlaskForm):
    ''' This seriously just chooses between closing the poll
        and refreshing the data '''

    refresh = SubmitField("Refresh Data")
    close = SubmitField("Close Polling")

####  These are for logging in and registering users  ####
class JoinSessionForm(FlaskForm):
    ''' Webform for joining a session. All the info on this can be found in the
        wtforms docs '''

    user = StringField("User", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sessionID = IntegerField('Session ID', validators=[DataRequired()])
    joinSession = SubmitField('Join Session')


class RegisterForm(FlaskForm):
        ''' Form for new users to register. '''

        user = StringField("User", validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        # This is just the cannonical 'confirm password' field.
        confirmPass = PasswordField(
            'Re-enter Password', validators=[DataRequired(), EqualTo('password')])
        register = SubmitField('Register')

        # Unfortunately we won't support duplicate usernames.
        # This function queries the database to ensure the entered
        # username isn't already taken.

        # This is a pretty interesting function
        # and funtions of the form validate_<fieldname> a a cool peice of wtforms
        def validate_user(self, user):
            u = User.query.filter_by(name = user.data).first()
            if u:
                raise ValidationError('Username unavailable.')

#This finds out how much money the players start with

class HostBlackJack(FlaskForm):
    money = IntegerField('Money for Game',validators=[DataRequired()])
    sessionID = IntegerField('Session ID', validators=[DataRequired()])
    submit = SubmitField('Submit')



"""
class PlayerForm(FlaskForm):
    a = BooleanField()
    b = BooleanField()
    submit = SubmitField('Submit Response(s)')
"""