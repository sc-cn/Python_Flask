# 盛放视图函数
from app import app
from models import Person, db


# 增加数据
@app.route('/add_person/')
def add_person():
    # 往数据库中保存数据。
    person_obj = Person()
    person_obj.name = 'zsfefe'
    person_obj.password = 'zs123'
    person_obj.age = 18
    person_obj.nickname = 'as'
    person_obj.gender = '男'
    person_obj.jobnum = 'zs111'
    person_obj.save()
    return 'add person...'


@app.route('/add_person2/')
def add_person2():
    person_obj = Person()
    person_obj.name = 'lisi'
    person_obj.password = 'ls123'
    person_obj.age = 18
    person_obj.nickname = 'ls'
    person_obj.gender = '男'
    person_obj.jobnum = 'ls111'

    person_obj1 = Person()
    person_obj1.name = 'ww'
    person_obj1.password = 'ww123'
    person_obj1.age = 20
    person_obj1.nickname = 'ww'
    person_obj1.gender = '男'
    person_obj1.jobnum = 'ww111'

    db.session.add_all([person_obj, person_obj1])
    db.session.commit()

    return 'add person2...'


# 查询
@app.route('/find/')
def find():
    # 1. all 表示查询所有,返回的是一个列表。
    person_obj_list = Person.query.all()  # [<Person 1>, <Person 2>, <Person 3>]
    print(person_obj_list)
    for person_obj in person_obj_list:
        print(person_obj.name)

    # [<obj:zs>, <obj:lisi>, <obj:ww>, <obj:zs>,]
    # person_obj = person_obj_list[0]
    # print(person_obj.id, person_obj.name)

    # 2.get() 获取,如果值不存在则返回None
    # person_obj = Person.query.get(10)
    # print(person_obj)  # <Person 1>

    # 3.filter() 过滤
    # 多个条件转换为sql的时候使用 and 链接。
    # ret = Person.query.filter(Person.age == 18, Person.name == 'zs').all()
    # print(ret)  # [<obj:zs>, <obj:lisi>, <obj:zs>]
    # 4.filter_by() : 使用数据库字段
    # ret = Person.query.filter_by(age=18).all()
    # print(ret)  # [<obj:zs>, <obj:lisi>, <obj:zs>]

    # 5.like 模糊查询
    # ret = Person.query.filter(Person.name.like('z%')).all()
    # print(ret)

    # 6.limit :限制
    # ret = Person.query.limit(2).all()
    # print(ret)

    # 7.offset 偏移
    # ret = Person.query.limit(2).offset(2).all()
    # print(ret)

    # 8.order_by 排序
    # ret = Person.query.order_by(Person.id.desc()).all()
    # print(ret)

    # 9.聚合查询 max、min、count...
    from sqlalchemy import func
    # ret = db.session.query(func.count(Person.id)).all()  # [(4,)]
    # print(ret)

    # 10.分组 group_by
    # ret = db.session.query(Person.gender, func.count(Person.id)).group_by(Person.gender)
    # print(ret)  # [('女', 2), ('男', 2)]

    # 11.逻辑查询
    # from sqlalchemy import and_, or_, not_
    # ret = Person.query.filter(or_(Person.age == 18, Person.gender == '女')).all()
    # print(ret)

    return 'find...'


# 修改
@app.route('/update/')
def update_person():
    person_obj = Person.query.filter(Person.id == 2).all()
    # print(person_obj)  # [<Person 2>]
    person_obj[0].name = 'zhaoliu'
    person_obj.update()
    return 'update...'


# 删除
@app.route('/delete/')
def delete():
    person_obj = Person.query.get(2)
    person_obj.delete()
    return 'delete...'
