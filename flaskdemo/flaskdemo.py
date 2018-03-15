from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
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