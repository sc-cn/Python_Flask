# 启动项目
from app import app
from models import db
from views import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)