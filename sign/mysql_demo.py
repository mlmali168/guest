#!/usr/bin/python
# _*_ coding:utf-8 _*_
# @time   :2018/8/3:11:51
# @author : mali
# @File   :mysql_demo.pf


from pymysql import cursors, connect

# 连接数据库

conn = connect(
    host='192.168.56.101',
    user='root',
    password='root',
    db='test1',
    charset='utf8',
    cursorclass=cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (real_name, phone, email, sign, event_id, create_time)' \
              ' VALUES ("tom", 18810011002, "tom@163.com",0,1,NOW());'
        cursor.execute(sql)
        # 提交事务
        conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "SELECT real_name,phone,email,sign FROM sign_guest WHERE phone = %s"
        cursor.execute(sql, ('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()




