from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "123"
app.config["UP_DIR"] = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "static/uploads/")

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000


from application.home import home as home_blueprint
from application.admin import admin as admin_blueprint
from application import models

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)

try:
    db.create_all()
except:
    pass
