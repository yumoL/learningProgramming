from . import home
from flask import render_template, redirect, url_for, flash, session,request
from application.home.forms import RegistForm, LoginForm,UserdetailForm,PwdForm,CommentForm
from application.models import User,Tag,Art,Comment,Artcol
from werkzeug.security import generate_password_hash
import datetime
from application import db
from functools import wraps 
from flask_login import login_user,logout_user,login_required,current_user


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
        # session["user"] = user.name
        # session["user_id"] = user.id
        login_user(user)
        return redirect(url_for("home.user"))
    return render_template("home/login.html", form=form)


@home.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.login"))


@home.route("/regist/", methods=["GET", "POST"])
def regist():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=db.func.current_timestamp()
        )
        db.session().add(user)
        db.session().commit()
        flash("Register suceeded", "ok")
    return render_template("home/register.html", form=form)

# change username
@home.route("/user/",methods=["GET","POST"])
@login_required
def user():
    form=UserdetailForm()
    user=User.query.get(int(current_user.id))
    if user is None:
        return redirect(url_for("home.index",page=1))
    if request.method=="GET":
        form.name.data=user.name
    if form.validate_on_submit():
        data=form.data
        name_count=User.query.filter_by(name=data["name"]).count()
        if data["name"]!=user.name and name_count==1:
            flash("Username is already existed","err")
            return redirect(url_for("home.user"))
        user.name=data["name"]
        db.session().add(user)
        db.session().commit()
        flash("Username has been changed","ok")
        return redirect(url_for("home.user"))
    return render_template("home/user.html",form=form)


#change password
@home.route("/pwd/",methods=["GET","POST"])
@login_required
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=current_user.name).first()
        if not user.check_pwd(data["old_pwd"]):
            flash("Wrong old password", "err")
            return redirect(url_for('home.pwd'))
        user.pwd = generate_password_hash(data["new_pwd"])
        db.session().add(user)
        db.session().commit()
        flash("Password has been changed, please login again", "ok")
        return redirect(url_for('home.logout'))
    return render_template("home/pwd.html",form=form)


@home.route("/comments/<int:page>/")
@login_required
def comments(page=None):
    if page is None:
        page = 1
    page_data = Comment.query.join(Art).join(User).filter(Art.id == Comment.art_id,
                                                            User.id == current_user.id).order_by(Comment.addtime.desc()).paginate(page=page, per_page=5)
    return render_template("home/comments.html",page_data=page_data)


@home.route("/<int:page>/",methods=["GET"])
def index(page=None):
    tags=Tag.query.all()
    page_data=Art.query
    #tagid
    tid=request.args.get("tid",0)
    if int(tid)!= 0:
        page_data=page_data.filter_by(tag_id=int(tid))
    #readnumber
    pm=request.args.get("pm",0)
    if int(pm)!=0:
        if int(pm)==1:
            page_data=page_data.order_by(
                Art.readnum.desc()
            )
        else:
            page_data=page_data.order_by(
                Art.readnum.asc()
            )
    #commentnumber
    cm=request.args.get("cm",0)
    if int(cm) != 0:
        if int(cm) == 1:
            page_data = page_data.order_by(
                Art.commentnum.desc()
            )
        else:
            page_data = page_data.order_by(
                Art.commentnum.asc()
            )
    if page is None:
        page=1
    page_data=page_data.paginate(page=page,per_page=5)
    p=dict(
        tid=tid,
        pm=pm,
        cm=cm,
    )
    return render_template("home/index.html",tags=tags,p=p,page_data=page_data)


@home.route("/search/<int:page>/")
def search(page=None):
    if page is None:
        page=1
    key=request.args.get("key","")
    art_count=Art.query.filter(
        Art.title.ilike('%'+key+'%')
    ).count()
    page_data=Art.query.filter(
        Art.title.ilike('%'+key+'%')
    ).order_by(
        Art.addtime.desc()
    ).paginate(page=page,per_page=10)
    page_data.key=key
    return render_template("home/search.html",art_count=art_count,key=key,page_data=page_data)

@home.route("/read/<int:id>/<int:page>/",methods=["GET","POST"])
def read(id=None,page=None):
    art=Art.query.join(Tag).filter(
        Tag.id==Art.tag_id,
        Art.id==int(id)
    ).first_or_404()

    if page is None:
        page = 1
    page_data = Comment.query.join(Art).join(User).filter(Art.id == art.id,
                                                            User.id == Comment.user_id).order_by(Comment.addtime.desc()).paginate(page=page, per_page=5)
    art.readnum=art.readnum+1
    form=CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        data=form.data
        comment=Comment(
            content=data["content"],
            addtime=db.func.current_timestamp(),
            art_id=art.id,
            user_id=current_user.id
        )
        db.session().add(comment)
        db.session().commit()
        
        art.commentnum=art.commentnum+1
        art.readnum=art.readnum-1
        db.session().add(art)
        db.session().commit()
        flash("Comment has been submited","ok")
        return redirect(url_for('home.read',id=art.id,page=1))
    db.session().add(art)
    db.session().commit()
    return render_template("home/read.html",art=art,form=form,page_data=page_data)

@home.route("/artcol/add/", methods=["GET"])
@login_required
def artcol_add():
    uid = request.args.get("uid", "")
    mid = request.args.get("mid", "")
    artcol = Artcol.query.filter_by(
        user_id=int(uid),
        art_id=int(mid)
    ).count()
    if artcol == 1:
        data = dict(ok=0)

    if artcol == 0:
        artcol = Artcol(
            user_id=int(uid),
            art_id=int(mid),
            addtime=db.func.current_timestamp(),
        )
        db.session.add(artcol)
        db.session.commit()
        data = dict(ok=1)
    import json
    return json.dumps(data)

@home.route("/artcol/<int:page>/")
@login_required
def artcol(page=None):
    if page is None:
        page = 1
    page_data = Artcol.query.join(
        Art
    ).join(
        User
    ).filter(
        Art.id == Artcol.art_id,
        User.id == current_user.id
    ).order_by(
        Artcol.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("home/artcol.html", page_data=page_data)

