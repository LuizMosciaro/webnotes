import os
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine,insert
from sqlalchemy.orm import Session
from datetime import datetime

#Base = automap_base()

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

#engine = create_engine({"MYSQLCONNECTION"})
#Base.prepare(autoload_with=engine)
#
#def add_user(user):
#    with Session(engine) as session:
#        with session.begin():
#            session.execute(insert(User).values(
#                email=user.email,
#                first_name=user.first_name,
#                password=user.password
#            ))
#
#def add_note(note,current_user):
#    with Session(engine) as session:
#        with session.begin():
#            session.execute(insert(Note).values(
#                texto=note.texto,
#                date=datetime.now(),
#                user_id=current_user.id
#            ))