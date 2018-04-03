from exts import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    telephon = db.Column(db.String(50),nullable=False)
    username = db.Column(db.Text(100),nullable=False)
    password = db.Column(db.Text(100),nullable=False)
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    autor =db.relationship('User',backref = db.backref('questions'))