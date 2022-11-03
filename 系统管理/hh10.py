import pymysql

def register(name, password):
    if name == '' or password =='':
        re = 0
        return re
    if name:
        db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
        sql = 'insert into hh1(name, password) value (%s, %s)'
        cur = db.cursor()
        cur.execute(sql,(name, password))
        db.commit()
        cur.close()
        db.close()
        return 1


def query1(name, password):
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    cur = db.cursor()
    sql = 'select * from hh1'
    cur.execute(sql)
    db.commit()
    kk = cur.fetchall()
    for i in range(len(kk)):
        if name == kk[i][0] and password == kk[i][1]:
            cur.close()
            db.close()
            return 1

def query2(name):
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    cur = db.cursor()
    sql = 'select * from hh2'
    cur.execute(sql)
    db.commit()
    kk = cur.fetchall()
    for i in range(len(kk)):
        if name == kk[i][0]:
            cur.close()
            db.close()
            return 1
    return 0
def establish(name, age, core):
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    cur = db.cursor()
    sql = 'insert into hh2(name, age, core) value(%s, %s, %s)'
    cur.execute(sql, (name, age, core))
    db.commit()
    sql = 'select * from hh2'
    cur.execute(sql)
    db.commit()
    kk = cur.fetchall()
    cur.close()
    db.close()
    return kk
def display():
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    cur = db.cursor()
    sql = 'select * from hh2'
    cur.execute(sql)
    db.commit()
    kk = cur.fetchall()
    cur.close()
    db.close()
    return kk
def delete(name):
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    cur = db.cursor()
    sql = 'delete from hh2 where name = %s'
    cur.execute(sql, name)
    db.commit()
    cur.close()
    db.close()
