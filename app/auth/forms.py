from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    """
    This is the Login Form class. It has the Form as a parent. When used in templating the wtf automatically
    generates a Form just as seen when we navigate towards /login page.
    """
    email = StringField('Email', validators=[Length(1, 64), Email()])
    password = PasswordField('Password', validators=[])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    """
    This is the Registration Form class. It has the Form as a parent. When used in templating the wtf automatically
    generates a Form just as seen when we navigate towards /register page.
    """
    # business_name = StringField('Business Name', validators=[Required(),
    #                                                Length(1, 64),
    #                                                Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
    #                                                       0,
    #                                                       'Usernames must have only letters, ''numbers, dots or underscores')])
    email = StringField('Email', validators=[
        Length(1, 64),
        Email()])
    username = StringField('Username', validators=[
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
               0,
               'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[])
    submit = SubmitField('Register')

    def validate_email(self, field):
        """
        :param field:
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        """
        :param field:
        :return:
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
