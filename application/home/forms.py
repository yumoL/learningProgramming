from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError,Length
from application.models import User


class RegistForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Username cannot be empty"),
            Length(min=3,max=100,message="The length of name should between 3-100 characters")
        ],

        description="Username",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter a username"
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Password cannot be empty"),
            Length(min=3,max=100,message="The length of password should between 3-100 characters")
        ],
        description="Password",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter your password"
        }
    )
    repwd = PasswordField(
        label="Password confirmation",
        validators=[
            DataRequired("Password cannot be empty"),
            EqualTo('pwd', message="Passwords are not same")
        ],
        description="Password confirmation",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter your password again"
        }
    )
    submit = SubmitField(
        'Register',
        render_kw={
            "class": "btn btn-lg btn success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("Username is already existed")


class LoginForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter your username")
        ],
        description="Username",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Username",
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Please enter your password")
        ],
        description="Password",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Password",
        }
    )
    submit = SubmitField(
        'Login',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )

class UserdetailForm(FlaskForm):
    name=StringField(
        label="Username",
        validators=[
            DataRequired("Please enter a username")
        ],
        render_kw={
            "class":"form-control",
            "placeholder":"Username"
        }
    )
    submit = SubmitField(
        'Save modification',
        render_kw={
            "class": "btn btn-success",
        }
    )

class PwdForm(FlaskForm):
    old_pwd=PasswordField(
        label="Old password",
        validators=[
            DataRequired("Please enter your old password")
        ],
        description="Old password",
        render_kw={
            "class":"form-control",
            "placeholder": "Old password"
        }
    )
    new_pwd=PasswordField(
        label="New password",
        validators=[
            DataRequired("Please enter your new password")
        ],
        description="New password",
        render_kw={
            "class":"form-control",
            "placeholder": "New password"
        }
    )
    submit = SubmitField(
        'Change password',
        render_kw={
            "class": "btn btn-success",
        }
    )

class CommentForm(FlaskForm):
    content=TextAreaField(
        label="Content",
        validators=[
            DataRequired("Please enter your commit"),
            Length(min=1,max=1000,message="The length of your comment should between 1-1000 characters")
        ],
        description="Some comment here...",
        render_kw={
            "class":"form-control",
            "id": "input_content",
            "rows":"5",
            "cols":"50"
        }
    )
    submit=SubmitField(
        'Submit comment',
        render_kw={
            "class":"btn btn-success",
            "id":"btn-sub"
        }
    )