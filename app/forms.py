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
    tim = SubmitField('Tims thing')

####  All of these are for the poll  ####
class AnswerForm(FlaskForm):
    answerText = StringField("Answer:", validators=[DataRequired()])

class QuestionForm(FlaskForm):
    questionText = StringField("Question:", validators=[DataRequired()])

    answers = FieldList(FormField(AnswerForm), min_entries = 1)

class PollForm(FlaskForm):
    sessionID = IntegerField('Session ID', validators=[DataRequired()])
    hideResults = BooleanField('Hide Results', default="checked")

    questions = FieldList(FormField(QuestionForm), min_entries = 0)

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
