
from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy

import os
app = Flask(__name__)


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///articles.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


from application.home import home as home_blueprint
from application.admin import admin as admin_blueprint
from application import models

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)


from application.home import views

#kirjautuminen
from application.models import User
from os import urandom
app.config["SECRET_KEY"]=urandom(32)

from flask_login import LoginManager
login_manager=LoginManager()
login_manager.init_app(app)

login_manager.login_view="home.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass
