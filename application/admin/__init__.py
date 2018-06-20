from flask import Blueprint
from application import app
from application.models import Admin
admin = Blueprint("admin",__name__)

import application.admin.views

#ylläpitäjän kirjautuminen


from flask_login import LoginManager
login_manager=LoginManager()
login_manager.init_app(app)

login_manager.login_view="admin.login"

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(admin_id)