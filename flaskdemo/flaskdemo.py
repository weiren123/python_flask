from flask import Flask, jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
# db = SQLAlchemy(app)
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(100),nullable=False)
#     content = db.Column(db.Text,nullable=False)
# db.create_all()

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        pass
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
    # article = Article.query.filter(Article.title == 'aaa').first()
    # db.session.delete(article)
    # db.session.commit()

    return 'Hello, World1111'
@app.route('/startimage/image.png')
def startimage():

    response = {
        'text': "success",
        'img': "https://dn-shimo-image.qbox.me/ZiiJ3jowWLEHccHq/image.png"
    }
    return jsonify(response), 200
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
