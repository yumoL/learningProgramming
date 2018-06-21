from flask import Flask
from application import db


class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, default=db.func.current_timestamp(),nullable=False)
    comments = db.relationship('Comment', backref='account')
    artcols=db.relationship('Artcol', backref='account')
    
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
    art = db.relationship('Art', backref='tag')

    def __repr__(self):
        return "<Tag %r>" % self.name


class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    text = db.Column(db.Text)
    readnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    addtime = db.Column(db.DateTime, default=db.func.current_timestamp(),nullable=False)
    comments = db.relationship("Comment", backref='art')
    artcols=db.relationship('Artcol', backref='art')

    def __repr__(self):
        return "<Art %r>" % self.title


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    addtime = db.Column(db.DateTime, default=db.func.current_timestamp(),nullable=False)
    art_id = db.Column(db.Integer, db.ForeignKey('art.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __repr__(self):
        return "<Comment %r>" % self.id


class Admin(db.Model):
    __tablename__="admin"
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100)) 
    is_super = db.Column(db.Integer)
    oplogs = db.relationship("Oplog", backref='admin')
    def __repr__(self):
        return "<Admin %r>" % self.name


class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True) 
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) 
    reason = db.Column(db.String(600)) 
    addtime = db.Column(db.DateTime,default=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return "<Oplog %r>" % self.id

class Artcol(db.Model):
    __tablename__ = "artcol"
    id = db.Column(db.Integer, primary_key=True)  
    art_id = db.Column(db.Integer, db.ForeignKey('art.id')) 
    user_id = db.Column(db.Integer, db.ForeignKey('account.id')) 
    addtime = db.Column(db.DateTime) 

    def __repr__(self):
        return "<Artcol %r>" % self.id