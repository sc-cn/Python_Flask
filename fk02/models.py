# 专门盛放 模型类
from app import db


# 将模型类中的 db.session..... 进行方法的封装，让程序更加健壮。


class Base(db.Model):
    __abstract__ = True  # 将Base改成抽象类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 保存数据
    def save(self):
        db.session.add(self)
        db.session.commit()

    # 修改操作
    def update(self):
        db.session.commit()

    # 删除
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Person(Base):
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    nickname = db.Column(db.String(32), nullable=True)
    gender = db.Column(db.String(32), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    jobnum = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(32), nullable=True)
    email = db.Column(db.String(32), nullable=True)
    picture = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(64), nullable=True)
    score = db.Column(db.Float, nullable=True)

    # def __repr__(self):
    #     return '<obj:{}>'.format(self.name)
