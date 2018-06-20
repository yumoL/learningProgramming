
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



from os import urandom
app.config["SECRET_KEY"]=urandom(32)

try:
    db.create_all()
except:
    pass
