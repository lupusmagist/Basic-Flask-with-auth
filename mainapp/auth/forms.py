from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember_me = BooleanField('remember me')
