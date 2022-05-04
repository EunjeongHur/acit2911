from wtforms import (
    StringField,
    PasswordField
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Regexp
from flask_login import current_user
from wtforms import ValidationError
from models import User

class login_form(FlaskForm):
    student_id=StringField(validators=[InputRequired(), Length(9)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])

class register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3,20, message="Please provide a valid username"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    student_id = StringField(
        validators=[
            InputRequired(),
            Length(9),
            Regexp(
                "[A]\d{8}",
                0,
                "Student ID must have Axxxxxxxx format"
            ),
        ]
    )
    pwd = PasswordField(validators=[InputRequired(), Length(8,72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8,72),
            EqualTo("pwd", message="Passwords must match"),
        ]
    )

    def validate_studentid(self, student_id):
        if User.query.filter_by(student_id=student_id.data).first():
            raise ValidationError("Student ID already registered")

    def validate_uname(self, username):
        if User.query_filter_by(username=username.data).first():
            raise ValidationError("Username already taken")