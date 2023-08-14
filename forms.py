from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=10)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=32)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), Length(min=8, max=32)]
    )


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
