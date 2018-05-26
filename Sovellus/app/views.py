from flask import render_template, redirect, flash, session, url_for, request
from app import app, db
from app.forms import LoginForm, RegisterForm, ArtForm, ArtEditForm
from app.models import User, Art
from werkzeug.security import generate_password_hash
import datetime
from functools import wraps 

#authority limitation


def user_login_req(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return login_req

#login


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["name"]
        flash("Login succeeded", "ok")
        return redirect("/art/list/1/")
    return render_template("login.html", title="Login", form=form)

#register


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        # save data
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.datetime.now()
        )
        db.session().add(user)
        db.session().commit()
        # short dialogue
        flash("Register succeeded, you can login now", "ok")
        return redirect("/login/")
    else:
        flash("Please enter correct information", "err")
    return render_template("register.html", title="Register", form=form)

#logout


@app.route("/logout/", methods=["GET"])
@user_login_req
def logout():
    session.pop("user", None)
    return redirect("/login/")

#publishing


@app.route("/art/add/", methods=["GET", "POST"])
@user_login_req
def art_add():
    form = ArtForm()
    if form.validate_on_submit():
        data = form.data
        #get user id
        user = User.query.filter_by(name=session["user"]).first()
        user_id = user.id
        #save data
        art = Art(
            title=data["title"],
            tag=data["tag"],
            user_id=user_id,
            content=data["content"],
            addtime=db.func.current_timestamp()
            #addtime=datetime.datetime.now().strftime("MM-DD-YYYY HH:MM:SS")
        )
        db.session().add(art)
        db.session().commit()
        flash("Publishing succeeded", "ok")
    return render_template("art_add.html", title="Article Publishing", form=form)

#editoring


@app.route("/art/edit/<int:id>", methods=["GET", "POST"])
@user_login_req
def art_edit(id):
    art = Art.query.get_or_404(int(id))
    form = ArtEditForm()
    if request.method == "GET":
        form.content.data = art.content
        form.tag.data = art.tag
    if form.validate_on_submit():
        data = form.data
        art.title = data["title"]
        art.tag = data["tag"]
        art.content = data["content"]
        db.session().add(art)
        db.session().commit()
        flash("Article has been successfully edited", "ok")
    return render_template("art_edit.html", form=form, title="Edit the article", art=art)

#delete


@app.route("/art/delete/<int:id>/", methods=["GET"])
@user_login_req
def art_del(id):
    art = Art.query.get_or_404(int(id))
    db.session().delete(art)
    db.session().commit()
    flash("Article <%s> has been successfully deleted" % art.title, "ok")
    return redirect("art/list/1/")

#list


@app.route("/art/list/<int:page>/", methods=["GET"])
@user_login_req
def art_list(page=None):
    if page is None:
        page = 1
    user = User.query.filter_by(name=session["user"]).first()
    page_data = Art.query.filter_by(
        user_id=user.id
    ).order_by(
        Art.addtime.desc()
    ).paginate(page=page, per_page=8)
    tag = [(1, "Action"), (2, "Comedy"), (3, "Science fiction"), (4, "Horror")]
    return render_template("art_list.html", title="Article List", page_data=page_data, tag=tag)
