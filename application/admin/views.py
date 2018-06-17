from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from application.admin.forms import LoginForm, TagForm, ArtForm, PwdForm
from application.models import Admin, Tag, Art, User, Comment, Oplog
from functools import wraps
from application import db, app
from sqlalchemy.sql import text
from datetime import datetime
import datetime
import os
import uuid

# admin's login time


@admin.context_processor
def tpl_extra():
    data = dict(
        online_time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    )
    return data


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


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
        session["admin_id"] = admin.id
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


@admin.route("/admin/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("admin.login"))

#change password


@admin.route("/admin/pwd/", methods=["GET", "POST"])
@admin_login_req
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(
            name=session["admin"], pwd=data["old_pwd"]).first()
        if not admin:
            flash("Wrong password", 'err')
            return redirect(url_for("admin.pwd"))

        admin.pwd = data["new_pwd"]
        db.session().add(admin)
        db.session().commit()
        flash("Password has been changed, please login again", "ok")
        return redirect(url_for('admin.logout'))

    return render_template("admin/pwd.html", form=form)


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
            addtime=db.func.current_timestamp()
        )
        db.session().add(tag)
        db.session().commit()
        flash("Tag is saved successfully", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"],
            reason="added tag %s" % data["name"],
            addtime=db.func.current_timestamp()
        )
        db.session().add(oplog)
        db.session().commit()
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
        oplog = Oplog(
            admin_id=session["admin_id"],
            reason="edited tag %s" % data["name"],
            addtime=datdb.func.current_timestamp()
        )
        db.session().add(oplog)
        db.session().commit()
        redirect(url_for('admin.tag_edit', id=id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


@admin.route("/admin/tag/del/<int:id>/", methods=["GET"])
@admin_login_req
def tag_del(id=None):
    art_count = Art.query.filter_by(tag_id=id).count()
    if art_count != 0:
        flash("Tag cannot be deleted, because it's related to an article", "err")
    else:
        tag = Tag.query.filter_by(id=id).first_or_404()
        db.session().delete(tag)
        db.session().commit()
        flash("Tag has been deleted successfully", "ok")
        oplog = Oplog(
            admin_id=session["admin_id"],
            reason="deleted tag %s" % tag.name,
            addtime=db.func.current_timestamp()
        )
        db.session().add(oplog)
        db.session().commit()
    return redirect(url_for('admin.tag_list', page=1))


@admin.route("/admin/art/add/", methods=["GET", "POST"])
@admin_login_req
def art_add():
    form = ArtForm()
    if form.validate_on_submit():
       data = form.data
       art = Art(
            title=data["title"],
            text=data["text"],
            readnum=0,
            commentnum=0,
            tag_id=int(data["tag_id"]),

            addtime=db.func.current_timestamp()
        )
       db.session().add(art)
       db.session().commit()
       flash("The article has been added successfully", "ok")
       oplog = Oplog(
            admin_id=session["admin_id"],
            reason="added article %s" % data["title"],
            addtime=db.func.current_timestamp()
        )
       db.session().add(oplog)
       db.session().commit()
       return redirect(url_for('admin.art_add'))
    return render_template("admin/art_add.html", form=form)


@admin.route("/admin/art/list/<int:page>/", methods=["GET"])
@admin_login_req
def art_list(page=None):
    if page is None:
        page = 1
    page_data = Art.query.join(Tag).filter(Tag.id == Art.tag_id).order_by(
        Art.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/art_list.html", page_data=page_data)


@admin.route("/admin/art/del/<int:id>/", methods=["GET"])
@admin_login_req
def art_del(id=None):
    art = Art.query.get_or_404(int(id))
    db.session().delete(art)
    db.session().commit()
    flash("Article is deleted", "ok")
    oplog = Oplog(
            admin_id=session["admin_id"],
            reason="deleted article %s" % art.title,
            addtime=db.func.current_timestamp()
        )
    db.session().add(oplog)
    db.session().commit()
    return redirect(url_for('admin.art_list', page=1))


@admin.route("/art/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def art_edit(id=None):
    form = ArtForm()
    art = Art.query.get_or_404(int(id))
    if request.method == "GET":
        form.text.data = art.text
        form.tag_id.data = art.tag_id

    if form.validate_on_submit():
       data = form.data
       art.title = data["title"]
       art.tag = data["tag"]
       art.text = data["text"]
       db.session().add(art)
       db.session().commit()
       flash("The article has bee successfully edited", "ok")
       oplog = Oplog(
            admin_id=session["admin_id"],
            reason="edited article %s" % data["title"],
            addtime=db.func.current_timestamp()
        )
       db.session().add(oplog)
       db.session().commit()
       return redirect(url_for('admin.art_edit', id=id))
    return render_template("admin/art_edit.html", form=form, art=art)


@admin.route("/admin/user/list/<int:page>/", methods=["GET"])
@admin_login_req
def user_list(page=None):
    if page is None:
        page == 1
    page_data = User.query.order_by(
        User.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/user_list.html", page_data=page_data)


@admin.route("/admin/user/view/<int:id>/", methods=["GET"])
@admin_login_req
def user_view(id=None):
    user = User.query.get_or_404(int(id))
    return render_template("admin/user_view.html", user=user)


@admin.route("/user/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def user_del(id=None):
    user = User.query.get_or_404(int(id))
    db.session().delete(user)
    db.session().commit()
    flash("User has been deleted", "ok")
    oplog = Oplog(
            admin_id=session["admin_id"],
            reason="deleted user %s" % user.name,
            addtime=db.func.current_timestamp()
        )
    db.session().add(oplog)
    db.session().commit()
    return redirect(url_for('admin.user_list', page=1))


@admin.route("/admin/comment/list/<int:page>/", methods=["GET"])
@admin_login_req
def comment_list(page=None):
    if page is None:
        page = 1
    page_data = Comment.query.join(Art).join(User).filter(Art.id == Comment.art_id,
                                                            User.id == Comment.user_id).order_by(Comment.addtime.desc()).paginate(page=page, per_page=10)

    return render_template("admin/comment_list.html", page_data=page_data)


@admin.route("/comment/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def comment_del(id=None):
    comment = Comment.query.get_or_404(int(id))
    db.session().delete(comment)
    db.session().commit()
    flash("Comment has been deleted", "ok")
    oplog = Oplog(
            admin_id=session["admin_id"],
            reason="deleted comment %s" % comment.content,
            addtime=db.func.current_timestamp()
        )
    db.session().add(oplog)
    db.session().commit()
    return redirect(url_for('admin.comment_list', page=1))


@admin.route("/admin/oplog/list/<int:page>/", methods=["GET"])
@admin_login_req
def oplog_list(page=None):
    if page is None:
        page = 1
    page_data = Oplog.query.join(
        Admin
    ).filter(
        Admin.id == Oplog.admin_id,
    ).order_by(
        Oplog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/oplog_list.html", page_data=page_data)



