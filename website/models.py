from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    texto = db.Column(db.String(1000),nullable=True)
    date = db.Column(db.Date,default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #user = User()

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    email = db.Column(db.String(150),nullable=False,unique=True)
    first_name = db.Column(db.String(150),nullable=False)
    password = db.Column(db.String(150),nullable=False)
    notes = db.relationship('Note') #aqui tem que ser N maiusculo