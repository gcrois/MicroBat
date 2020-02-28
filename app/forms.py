# This is where we store web forms.
# Things like the join session form for users.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired

# Webform for joining a session.
class JoinSessionForm(FlaskForm):
    user = StringField("User", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sessionID = IntegerField('Session ID', validators=[DataRequired()])
    joinSession = SubmitField('Join Session')
