from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from application.admin.forms import LoginForm, TagForm, MovieForm
from application.models import Admin, Tag, Movie
from functools import wraps
from werkzeug.utils import secure_filename
from application import db, app
from datetime import datetime
import datetime
import os
import uuid

# no login->nothing


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# change filename


def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
        str(uuid.uuid4().hex+fileinfo[-1])
    return filename


@admin.route("/admin/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route("/admin/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(
            name=data["account"], pwd=data["pwd"]).first()
        if not admin:
            flash("No such username or password", 'err')
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


@admin.route("/admin/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin.login"))


@admin.route("/admin/pwd/")
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")


@admin.route("/admin/tag/add/", methods=["GET", "POST"])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["name"]).count()
        if tag > 0:
            flash("This tag is already existed", "err")
            return redirect(url_for('admin.tag_add'))
        tag = Tag(
            name=data["name"],
            addtime=datetime.datetime.now()
        )
        db.session().add(tag)
        db.session().commit()
        flash("Tag is saved successfully", "ok")
        redirect(url_for('admin.tag_add'))
    return render_template("admin/tag_add.html", form=form)


@admin.route("/admin/tag/list/<int:page>/", methods=["GET"])
@admin_login_req
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=6)
    return render_template("admin/tag_list.html", page_data=page_data)


@admin.route("/admin/tag/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
def tag_edit(id=None):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data["name"]).count()
        if tag.name != data["name"] and tag_count == 1:
            flash("This tag is already existed", "err")
            return redirect(url_for('admin.tag_edit', id=id))
        tag.name = data["name"]
        db.session().add(tag)
        db.session().commit()
        flash("Tag is edited successfully", "ok")
        redirect(url_for('admin.tag_edit', id=id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


@admin.route("/admin/tag/del/<int:id>/", methods=["GET"])
@admin_login_req
def tag_del(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session().delete(tag)
    db.session().commit()
    flash("Tag has been deleted successfully", "ok")
    return redirect(url_for('admin.tag_list', page=1))


@admin.route("/admin/movie/add/", methods=["GET", "POST"])
@admin_login_req
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        file_url = secure_filename(form.url.data.filename)
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        url = change_filename(file_url)
        form.url.data.save(app.config["UP_DIR"]+url)
        movie = Movie(
            title=data["title"],
            url=url,
            info=data["info"],
            playnum=0,
            commentnum=0,
            tag_id=int(data["tag_id"]),
            area=data["area"],
            release_time=(data["release_time"]),
            length=data["length"],
            addtime=datetime.datetime.now()
        )
        db.session().add(movie)
        db.session().commit()
        flash("The movie has been added successfully", "ok")
        return redirect(url_for('admin.movie_add'))
    return render_template("admin/movie_add.html", form=form)


@admin.route("/admin/movie/list/<int:page>/", methods=["GET"])
@admin_login_req
def movie_list(page=None):
    if page is None:
        page = 1
    page_data = Movie.query.join(Tag).filter(Tag.id == Movie.tag_id).order_by(
        Movie.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/movie_list.html", page_data=page_data)


@admin.route("/admin/movie/del/<int:id>/", methods=["GET"])
@admin_login_req
def movie_del(id=None):
    movie = Movie.query.get_or_404(int(id))
    db.session().delete(movie)
    db.session().commit()
    flash("Movie is deleted", "ok")
    return redirect(url_for('admin.movie_list', page=1))


@admin.route("/movie/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def movie_edit(id=None):
    form = MovieForm()
    form.url.validators = []
    movie = Movie.query.get_or_404(int(id))
    if request.method == "GET":
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id

    if form.validate_on_submit():
        data = form.data
        movie_count = Movie.query.filter_by(title=data["title"]).count()
        if movie_count == 1 and movie.title != data["title"]:
            flash("The title has already existed", "err")
            return redirect(url_for('admin.movie_edit', id=id))

        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")

        if form.url.data != "":
            file_url = secure_filename(form.url.data.filename)
            movie.url = change_filename(file_url)
            form.url.data.save(app.config["UP_DIR"] + movie.url)

        movie.tag_id = data["tag_id"]
        movie.info = data["info"]
        movie.title = data["title"]
        movie.area = data["area"]
        movie.length = data["length"]
        movie.release_time = data["release_time"]
        movie.addtime = datetime.datetime.now()
        db.session().add(movie)
        db.session().commit()
        flash("The movie has bee successfully edited", "ok")
        return redirect(url_for('admin.movie_edit', id=id))
    return render_template("admin/movie_edit.html", form=form, movie=movie)


@admin.route("/admin/user/list/")
@admin_login_req
def user_list():
    return render_template("admin/user_list.html")


@admin.route("/admin/user/view/")
@admin_login_req
def user_view():
    return render_template("admin/user_view.html")


@admin.route("/admin/comment/list/")
@admin_login_req
def comment_list():
    return render_template("admin/comment_list.html")


@admin.route("/admin/moviecol/list/")
@admin_login_req
def moviecol_list():
    return render_template("admin/moviecol_list.html")


@admin.route("/admin/oplog/list/")
@admin_login_req
def oplog_list():
    return render_template("admin/oplog_list.html")
