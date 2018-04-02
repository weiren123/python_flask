from flask import Flask, jsonify,render_template,request,redirect,url_for,session
import config
from models import User
from exts import db
app = Flask(__name__)
app.config.from_object(config)
# db = SQLAlchemy(app)
# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(100),nullable=False)
#     content = db.Column(db.Text,nullable=False)
# db.create_all()
db.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephon == telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return "手机号或密码错误！"

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephon = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephon == telephon).first()
        if user:
            return "该手机号已被注册，请更换手机号!"
        else:
            if password1 != password2:
                return "两次输入的密码不一致，请核对后重新输入！"
            else:
                user = User(telephon = telephon,username =username,password = password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}
@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))
@app.route('/question')
def question():
    if request.method == 'GET':
         return render_template('question.html')
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
