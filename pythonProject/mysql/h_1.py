import pymysql
import pandas as pd
df = pd.read_excel(r'E:\Desktop\升降屏向上.xlsx')
ss = df.shape[0]
db = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',  # 在这里输入用户名
    password='huhao',  # 在这里输入密码
    charset='utf8mb4',
    database='justtest'
)
cursor = db.cursor()

tablename = 'user'
sql = "drop table if exists user"
cursor.execute(sql)
sql = 'create table  {} (id varchar(20) not null, name varchar(20) not null, primary key(id), age int)'.format(tablename)
cursor.execute(sql)
for i in range(1,ss):
    sql = 'insert into user(id,name,age) values ({},{},{})'.format(df.iloc[i,4],df.iloc[i,5],df.iloc[i,6])
    cursor.execute(sql)
sql = 'select * from user'
tt = cursor.execute(sql)
tt1 = cursor.fetchall()
print(tt1)