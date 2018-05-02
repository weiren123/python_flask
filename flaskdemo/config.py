#encoding:utf-8
import os
DEBUG = True
# 随机产生24个字节的字符串
SECRET_KEY = os.urandom(24)
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskdemo'
USERNAME = 'root'
PASSWORD = '1234'
DB_URI = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'I have a dream'
UPLOADED_PHOTOS_DEST= os.getcwd()+'/static/image'

app_key = u'552ff435c35340d1e6fc8be8'
master_secret = u'd3ee34a00b9ba28b73da6853'

