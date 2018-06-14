from . import home
from flask import render_template, redirect, url_for, flash, session,request
from application.home.forms import RegistForm, LoginForm,UserdetailForm,PwdForm,CommentForm
from application.models import User,Tag,Movie,Comment
from werkzeug.security import generate_password_hash
import datetime
from application import db
from functools import wraps 

# autorisointi
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
    return redirect(url_for("home.login"))


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

# change username
@home.route("/user/",methods=["GET","POST"])
@user_login_req
def user():
    form=UserdetailForm()
    user=User.query.get(int(session["user_id"]))
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
@user_login_req
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=session["user"]).first()
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
@user_login_req
def comments(page=None):
    if page is None:
        page = 1
    page_data = Comment.query.join(Movie).join(User).filter(Movie.id == Comment.movie_id,
                                                            User.id == session["user_id"]).order_by(Comment.addtime.desc()).paginate(page=page, per_page=5)
    return render_template("home/comments.html",page_data=page_data)


@home.route("/<int:page>/",methods=["GET"])
def index(page=None):
    tags=Tag.query.all()
    page_data=Movie.query
    #tagid
    tid=request.args.get("tid",0)
    if int(tid)!= 0:
        page_data=page_data.filter_by(tag_id=int(tid))
    #playednumber
    pm=request.args.get("pm",0)
    if int(pm)!=0:
        if int(pm)==1:
            page_data=page_data.order_by(
                Movie.playnum.desc()
            )
        else:
            page_data=page_data.order_by(
                Movie.playnum.asc()
            )
    #commentnumber
    cm=request.args.get("cm",0)
    if int(cm) != 0:
        if int(cm) == 1:
            page_data = page_data.order_by(
                Movie.commentnum.desc()
            )
        else:
            page_data = page_data.order_by(
                Movie.commentnum.asc()
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
    movie_count=Movie.query.filter(
        Movie.title.ilike('%'+key+'%')
    ).count()
    page_data=Movie.query.filter(
        Movie.title.ilike('%'+key+'%')
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page,per_page=10)
    page_data.key=key
    return render_template("home/search.html",movie_count=movie_count,key=key,page_data=page_data)

@home.route("/play/<int:id>/<int:page>/",methods=["GET","POST"])
def play(id=None,page=None):
    movie=Movie.query.join(Tag).filter(
        Tag.id==Movie.tag_id,
        Movie.id==int(id)
    ).first_or_404()

    if page is None:
        page = 1
    page_data = Comment.query.join(Movie).join(User).filter(Movie.id == movie.id,
                                                            User.id == Comment.user_id).order_by(Comment.addtime.desc()).paginate(page=page, per_page=5)
    movie.playnum=movie.playnum+1
    form=CommentForm()
    if "user" in session and form.validate_on_submit():
        data=form.data
        comment=Comment(
            content=data["content"],
            addtime=datetime.datetime.now(),
            movie_id=movie.id,
            user_id=session["user_id"]
        )
        db.session().add(comment)
        db.session().commit()
        
        movie.commentnum=movie.commentnum+1
        db.session().add(movie)
        db.session().commit()
        flash("Comment has been submited","ok")
        return redirect(url_for('home.play',id=movie.id,page=1))
    db.session().add(movie)
    db.session().commit()
    return render_template("home/play.html",movie=movie,form=form,page_data=page_data)
