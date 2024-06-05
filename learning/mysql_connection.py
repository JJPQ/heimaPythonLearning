from pymysql import Connection

# 构建连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='MJ18895581108'
)

# 执行非查询性质的sql
# cursor=conn.cursor()      # 获取到游标对象
#
# conn.select_db('study')
#
# cursor.execute('create table python(id int,name varchar(10));')

# 执行查询性质的sql
# cursor=conn.cursor()      # 获取到游标对象
#
# conn.select_db('study')
#
# cursor.execute('select * from student')
#
# result:tuple=cursor.fetchall()
#
# for i in result:
#     print(i)

# 执行插入操作
cursor = conn.cursor()  # 获取到游标对象

conn.select_db('study')

cursor.execute("insert into student values(5,'mj',18,'M')")

# 通过commit方法确认
conn.commit()

conn.close()
