from flask import Flask
from application import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, nullable=False)
    comments = db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        return "<User %r>" % self.name
    
    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd,pwd)


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, nullable=False)
    movies = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return "<Tag %r>" % self.name


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    area = db.Column(db.String(255))
    release_time = db.Column(db.String(10))
    length = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, nullable=False)
    comments = db.relationship("Comment", backref='movie')
    moviecols = db.relationship("Moviecol", backref='movie')

    def __repr__(self):
        return "<Movie %r>" % self.title


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    addtime = db.Column(db.DateTime, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Comment %r>" % self.id


# # movie collection
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Moviecol %r>" % self.id

class Admin(db.Model):
    __tablename__="admin"
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100)) 
    oplogs = db.relationship("Oplog", backref='admin')
    def __repr__(self):
        return "<Admin %r>" % self.name


class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True) 
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) 
    reason = db.Column(db.String(600)) 
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Oplog %r>" % self.id
