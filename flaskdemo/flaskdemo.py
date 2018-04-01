from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
    # article = Article(title = 'aaa',content = 'bbb')
    # db.session.add(article)
    # db.session.commit()
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print(article)
    # article = Article.query.filter(Article.title == 'aaa').first()
    # article.title = 'new title'
    # db.session.commit()
    article = Article.query.filter(Article.title == 'aaa').first()
    db.session.delete(article)
    db.session.commit()

    return 'Hello, World1111'
@app.route('/startimage/image.png')
def startimage():

    response = {
        'text': "success",
        'img': "https://dn-shimo-image.qbox.me/ZiiJ3jowWLEHccHq/image.png"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
