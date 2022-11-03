import pymysql


def found(name, age, core):
    db = pymysql.connect(host='127.0.0.1', user='root', password='huhao', database='hh1')
    print('连接成功')
    cur = db.cursor()
    sql = 'insert into hh1(name, age, core) values(%s, %s, %s)'
    cur.execute(sql, (name,age,core))
    db.commit()
    sql = 'select * from hh1'
    cur.execute(sql)
    k = cur.fetchall()
    for i in range(len(k)):
        for j in range(len(k[i])):
            print(k[i][j],end='\t\t\t')
        print('\n')
    cur.close()
    db.close()


if __name__ == '__main__':
    found('xiaohong', 14, 77)
