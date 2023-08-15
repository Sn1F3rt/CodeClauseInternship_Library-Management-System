from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    author = StringField("Author", validators=[DataRequired(), Length(max=100)])
    year = IntegerField(
        "Year", validators=[DataRequired(), NumberRange(min=1000, max=9999)]
    )
