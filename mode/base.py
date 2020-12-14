
#pymysql的作用

#通过pymysql操作数据的步骤:

#1.导包： import pymysql

#2. 建立连接： conn = pymysql.connect()

#  connect()参数：
#   1）user : 代表连接数据库的用户名
#   2）password : 连接数据库的密码
#   3）host : 连接数据库的主机名
#   4）database : 连接的数据库
#   5）port : 连接的端口
#   6）charset : 设置编码

#3.建立游标对象 : cursor == conn.cursor()

#4.执行sql语句 : cursor.execute(sql)

   #查询一条数据:cursor.getone()
   #查询所有数据:cursor.getall()


#5.关闭游标对象 : cursor.close()

#6.关闭连接对象 : conn.close()



import pymysql

from setting import  DB_CONFIG

class Mysql():

    #构造方法
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)

    #实现一个增加，修改和删除的方法
    def update(self,sql):
        print("接受到的sql语句:{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        finally:
            if self.conn:
                self.conn.close()


    #查询数据的方法

    def get_all(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()


if __name__ == "__main__":
    sql = "select * from students where age > 30"
    sql1 = "update students set class = '7班' where studentNo = 12"
    mysql = Mysql()
    result = mysql.get_all(sql)
    print(result)
    #mysql.update(sql1)