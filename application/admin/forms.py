from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from application.models import Admin, Tag


class LoginForm(FlaskForm):
    account = StringField(
        label="Username",
        validators=[
            DataRequired("Username cannot be empty")
        ],
        description="Username",
        render_kw={
            "class": "form-control",
            "placeholder": "Username"
            # "required":"required"
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
            "placeholder": "Password"
            # "required":"required"
        }
    )
    submit = SubmitField(
        "Login",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


class TagForm(FlaskForm):
    name = StringField(
        label="Name",
        validators=[
            DataRequired("Please enter the tag")
        ],
        description="Tag",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "Tag name"
        }

    )
    submit = SubmitField(
        "Edit",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label="Title",
        validators=[
            DataRequired("Please enter the name of te movie")
        ],
        description="Title",
        render_kw={
            "class": "form-control",
            "placeholder": "title"
        }
    )
    url = FileField(
        label="File",
        validators=[
            DataRequired("Please upload your file")
        ],
        description="File"
    )
    info = TextAreaField(
        label="Info",
        validators=[
            DataRequired("Please enter the info of the movie")
        ],
        description="info",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    tag_id = SelectField(
        label="Tag",
        validators=[
            DataRequired("Please select a tag")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description="Tag",
        render_kw={
            "class": "form-control",
        }
    )
    area = StringField(
        label="Area",
        validators=[
            DataRequired("Please enter the Area")
        ],
        description="Area",
        render_kw={
            "class": "form-control",
            "placeholder": "Area"
        }
    )
    length = StringField(
        label="Length",
        validators=[
            DataRequired("Please enter the length")
        ],
        description="Length",
        render_kw={
            "class": "form-control",
            "placeholder": "Length"
        }
    )
    release_time = StringField(
        label="Release time",
        validators=[
            DataRequired("Please enter the release time")
        ],
        description="Release time",
        render_kw={
            "class": "form-control",
            "placeholder": "yyyy-mm-dd",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )

class PwdForm(FlaskForm):
    old_pwd=PasswordField(
        label="Old password",
        validators=[
            DataRequired("PLease enter your old password")
        ],
        description="Old password",
        render_kw={
            "class":"form-control",
            "placeholder":"Old password"
        }
    )
    new_pwd=PasswordField(
        label="New password",
        validators=[
            DataRequired("PLease enter new password")
        ],
        description="New password",
        render_kw={
            "class":"form-control",
            "placeholder":"New password"
        }
    )
    submit = SubmitField(
        'Edit',
        render_kw={
            "class": "btn btn-primary",
        }
    )