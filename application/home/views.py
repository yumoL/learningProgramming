from . import home
from flask import render_template, redirect, url_for, flash, session,request
from application.home.forms import RegistForm, LoginForm
from application.models import User
from werkzeug.security import generate_password_hash
import datetime
from application import db
from functools import wraps 


def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@home.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if user is None:
            flash("No such user","err")
            return redirect(url_for("home.login"))
        if not user.check_pwd(data["pwd"]):
            flash("Incorrect password", "err")
            return redirect(url_for("home.login"))
        session["user"] = user.name
        session["user_id"] = user.id
        return redirect(url_for("home.user"))
    return render_template("home/login.html", form=form)


@home.route("/logout/")
@user_login_req
def logout():
    session.pop("user",None)
    session.pop("user_id",None)
    return redirect(url_for("home/login.html"))


@home.route("/regist/", methods=["GET", "POST"])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.datetime.now()
        )
        db.session().add(user)
        db.session().commit()
        flash("Register suceeded", "ok")
    return render_template("home/register.html", form=form)


@home.route("/user/")
@user_login_req
def user():
    return render_template("home/user.html")


@home.route("/pwd/")
@user_login_req
def pwd():
    return render_template("home/pwd.html")


@home.route("/comments/")
@user_login_req
def comments():
    return render_template("home/comments.html")


@home.route("/moviecol/")
@user_login_req
def moviecol():
    return render_template("home/moviecol.html")


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/search/")
def search():
    return render_template("home/search.html")


@home.route("/play/")
def play():
    return render_template("home/play.html")
