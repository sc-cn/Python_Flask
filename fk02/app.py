# 项目配置操作 例如 链接数据等等
from flask import Flask
import os
import pymysql

pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'fk02.db')


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/fk01'
# # 在未来会被禁用，flask里面有事件系统，但是一般程序用不到事件系统，建议关闭，使用False
# # 如果说开启，会增加大量开销。
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
