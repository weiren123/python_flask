
from datetime import datetime
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
#     telephon = db.Column(db.String(50),nullable=False)
#     username = db.Column(db.Text(100),nullable=False)
#     password = db.Column(db.Text(100),nullable=False)
from exts import db


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    answer_id = db.Column(db.Integer,default=0)
    autor_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    autor =db.relationship('User',backref = db.backref('questions'))

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    autor_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    question = db.relationship('Question',backref =db.backref('answers'))
    autor = db.relationship('User',backref = db.backref('answers'))
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username = db.Column(db.Text(100),nullable=False)
    age = db.Column(db.String(100),nullable=False)
    telephon = db.Column(db.String(100),nullable=False)
    password = db.Column(db.Text(100),nullable=False)
    usertype = db.Column(db.String(100),nullable=False)
    sex = db.Column(db.Text(100),nullable=False)
    avatar = db.Column(db.Text,nullable=True)
    birthday =db.Column(db.String(100),nullable=False)
    userbgimg = db.Column(db.Text,nullable=True)
