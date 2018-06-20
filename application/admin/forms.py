from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError,Length
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
            DataRequired("Please enter the tag"),
            Length(min=1,max=100,message="The length of a tag should betweem 1-100 characters")
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


class ArtForm(FlaskForm):
    title = StringField(
        label="Title",
        validators=[
            DataRequired("Please enter your title "),
            Length(min=1,max=255,message="The length of a title should betweem 1-100 characters")
        ],
        description="Title",
        render_kw={
            "class": "form-control",
            "placeholder": "title"
        }
    )
    
    tag_id = SelectField(
        label="Tag",
        validators=[
            DataRequired("Please select a tag, or just go to add a new tag")
        ],
        coerce=int,
        
        description="Tag",
        render_kw={
            "class": "form-control",
        }
    )
    text = TextAreaField(
        label="Content",
        validators=[
            DataRequired("Content cannnot be empty"),
             Length(min=1,max=100000,message="The length of your content should betweem 1-100000 characters")
        ],
        description="Content",
        render_kw={
            "Style": "height:300px; width:500px;",
            "id": "content"
        }

    )
    submit = SubmitField(
        'Submit',
        render_kw={
            "class": "btn btn-primary",
        }
    )
    def __init__(self,*args,**kwargs):
        super(ArtForm,self).__init__(*args,*kwargs)
        self.tag_id.choices=[(v.id, v.name) for v in Tag.query.all()]

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


