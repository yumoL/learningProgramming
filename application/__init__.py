from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"]="123"
app.config["UP_DIR"]=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
db = SQLAlchemy(app)




from application.home import home as home_blueprint
from application.admin import admin as admin_blueprint
from application import models

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)

db.create_all()