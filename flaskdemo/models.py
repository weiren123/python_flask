from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    telephon = db.Column(db.String(50),nullable=False)
    username = db.Column(db.Text(100),nullable=False)
    password = db.Column(db.Text(100),nullable=False)