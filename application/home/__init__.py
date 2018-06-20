from flask import Blueprint
from application import app
from application.models import User

home = Blueprint("home",__name__)

import application.home.views


#normaalin kätyttäjän kirjautuminen


from flask_login import LoginManager
login_manager=LoginManager()
login_manager.init_app(app)

login_manager.login_view="home.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)