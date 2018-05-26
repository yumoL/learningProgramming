from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Username cannot be empty")
        ],
        description="Username",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter your username"
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Password cannot be empty")
        ],
        description="Password",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter your password"
        }

    )
    submit = SubmitField(
        "Login",
        render_kw={
            "class": "btn btn-primary" 
        }
    )

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if user == None:
            raise ValidationError("No such user name")

        elif not user.check_pwd(pwd):
            raise ValidationError("Incorrect password")


class RegisterForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Username cannot be empty")
        ],
        description="Username",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter your username"
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Password cannot be empty")
        ],
        description="Password",
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter your password"
        }

    )
    repwd = PasswordField(
        label="Confirm your password",
        validators=[
            DataRequired("Password confirmation cannot be empty"),
            EqualTo('pwd', message="Passwords are not same")
        ],
        description="Confirm your password",
        render_kw={
            "class": "form-control",
            "placeholder": "Please confirm your password"
        }

    )
    submit = SubmitField(
        "Register",
        render_kw={
            "class": "btn btn-success"
        }
    )
    # check if username has already existed

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError(
                "Username has already existed, pleace choose another username")


class ArtForm(FlaskForm):
    title = StringField(
        label="Title",
        description="title",
        validators=[
            DataRequired("Title cannot be empty")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter a title"
        }
    )
    tag = SelectField(
        label="Tag",
        description="Tag",
        validators=[
            DataRequired("Tag cannot be empty")
        ],
        choices=[(1, "Action"), (2, "Comedy"),
                 (3, "Science fiction"), (4, "Horror")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    content = TextAreaField(
        label="Content",
        validators=[
            DataRequired("Content cannnot be empty")
        ],
        description="Content",
        render_kw={
            "Style": "height:300px;",
            "id": "content"
        }

    )
    submit = SubmitField(
        "Publish the article",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class ArtEditForm(FlaskForm):
    id = IntegerField(
        label="number",
        validators=[DataRequired("Number cannot be empty")
                    ],
    )
    title = StringField(
        label="Title",
        description="title",
        validators=[
            DataRequired("Title cannot be empty")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Please enter a title"
        }
    )
    tag = SelectField(
        label="Tag",
        description="Tag",
        validators=[
            DataRequired("Tag cannot be empty")
        ],
        choices=[(1, "Action"), (2, "Comedy"),
                 (3, "Science fiction"), (4, "Horror")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control"
        }
    )
    content = TextAreaField(
        label="Content",
        validators=[
            DataRequired("Content cannnot be empty")
        ],
        description="Content",
        render_kw={
            "Style": "height:300px;",
            "id": "content"
        }

    )
    submit = SubmitField(
        "Edit the article",
        render_kw={
            "class": "btn btn-primary"
        }
    )
