from flask import Blueprint

admin = Blueprint("admin",__name__)

import application.admin.views