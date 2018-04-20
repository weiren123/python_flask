from PIL import Image
from flask import Flask, jsonify, render_template, request, url_for, session, redirect, g, send_file, Response
from functools import wraps

from io import BytesIO

import config
from models import User,Question,Answer
from exts import db
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            response = {
                'code': "302",
                'msg':"login"
            }
            # return redirect(url_for('login', next=request.url))
            return jsonify(response),200
        return f(*args, **kwargs)
    return decorated_function
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first
        if user:
            g.user = user
    else:
        g.user = None
@app.route('/')
def index():
    content = {
        'questions':Question.query.all()
    }
    return render_template('index.html',**content)
@app.route('/questionlist/',methods=['POST'])
def getQuestionList():
    # userid = session.get('user_id')
    userid = request.form.get('user_id')
    question = Question.query.filter(Question.answer_id == userid).all()
    if question:
        response = {
            'code': "success",
            "msg": "成功"
        }
        data = []
        for questionInfo in question:
            item = {
                "title": questionInfo.title,
                "content": questionInfo.content,
            }
            data.append(item)
            response['body'] = data
        return jsonify(response), 200
    else:
        response = {
            "code": "error",
            "msg": "没有问题",
        }
        return jsonify(response), 200


@app.route('/userinfo_list/')
def getUserList():
    # user_id = session.get('user_id')

    user = User.query.filter(User.usertype== '1').all()
    if user:
        response = {
            "code": "success",
            "msg": "成功"
        }
        data =[]
        for userinfo in user:
            item = {
                'username': userinfo.username,
                'age': userinfo.age,
                'avatar': userinfo.avatar,
                'usertype': userinfo.usertype,
                'userid': userinfo.id
             }
            data.append(item)
        response['body'] = data
        resp = Response("")
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return jsonify(response), 200,{'Content-Type': 'application/json'}
    else:
        response = {
            "code": "error",
            "msg": "没有用户"
        }
        return jsonify(response), 200
@app.route('/login/',methods=['GET','POST'])
def login():
    # if request.method == 'POST'| request.module == 'GET':
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephon == telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            response = {
                'code': "success",
                'msg': "登陆成功!"
            }
            return jsonify(response),200
        else:
            response = {
                'code': "error",
                'msg': "手机号或密码错误!"
            }
            return jsonify(response),200

@app.route('/regist/',methods=['POST'])
def regist():
        # response = request.from_values('telephone')
        # print(str(response))
        telephon = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.telephon == telephon).first()
        if user:
            response = {
                'code': "error",
                'msg':"该手机号已被注册，请更换手机号!"
            }
            return jsonify(response),200
        else:
            if password1 != password2:
                response = {
                    'code': "error",
                    'msg': "两次输入的密码不一致，请核对后重新输入！"
                }
                return jsonify(response),200
            else:
                user = User(telephon = telephon,username =username,password = password1,age = "18",usertype = "1",
                            sex = "0",birthday = "1991-08-09" )
                db.session.add(user)
                db.session.commit()
                response = {
                    'code': "success",
                    'msg': "注册成功！"
                }
                return jsonify(response),200
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
@app.route('/question/',methods=['POST'])
@login_required
def question():
        answer_id =request.form.get('answer_id')
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = session.get('user_id')
        question = Question(title=title, content=content,autor_id = user_id,answer_id = answer_id)
        db.session.add(question)
        db.session.commit()
        response = {
            'code': "success",
            'msg': "发送成功！"
        }
        return jsonify(response),200
@app.route('/detail/<question_id>/')
def detail(question_id):
    question = Question.query.filter(Question.id == question_id).first()

    return render_template('detail.html',question = question)
@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():

    add_answer = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    answer = Answer(content =add_answer)
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    answer.autor = user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id = question_id))
# @app.route('/answers/')
# def answers():
#     content = {
#         'answers':Answer.query.all()
#     }
#     return render_template('detail.html',**content)
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
@app.route('/startimage/')
def startimage():
    img = Image.open('static/image/v1.jpg')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    response = {
        'text': "success",
        'img': byte_io
    }
    return jsonify(response), 200
@app.route("/image")
def test_qrcode():
    img = Image.open('static/image/v1.jpg')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run()
