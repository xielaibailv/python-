import pymysql
# import PyMysqlDB
# import mysqldb

#打开数据库连接
def mysql():
    db = pymysql.connect(
        host='192.168.1.157',
        user='root',
        password='000000',
        port=3306,
        charset='utf8',
        db1='sanhua',
        db2 = 'sanhua_electric')

    #使用cursor()方法获取操作游标
    cursor = db.cursor()

    #使用execute方法执行sql语句
    #查询某一块表某一段时间的日需量
    cursor.execute("select * from db1.t_cal_day_avg where device_id='1b758f86e1004000' and create_time BETWEEN '2018-11-08 00:00:00' and '2018-11-08 23:59:59'" )
    cursor.execute("select billingId from t_billing where mdmid = '1c588f4b2e000000'")

    #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    #fetchall():接收全部的返回结果行.
    #rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
    data = cursor.fetchone()
    print(data)