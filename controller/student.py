

from mode.base import Mysql

class Student():


    def __init__(self):
        self.mysql = Mysql()



    #添加学生的业务
    def add_student(self,*args):
        lst = list(args)
        while len(lst) <= 6:
            lst.append('')
        sql = "insert into students(studentNo,name,age,sex,class,card,city) \
               values('{}','{}','{}','{}','{}','{}','{}')".format(*lst)
        result = self.mysql.update(sql)
        if not result:
            print("添加学生成功")
        else:
            print("添加学生失败")



    #删除学生的业务
    def mox_student(self,studentNo):
        sql = "delete from students where studentNo = '{}'".format(studentNo)
        result = self.mysql.update(sql)
        if not result:
            print("删除信息成功")
        else:
            print("删除信息失败")



    #修改学生的业务
    def mod_student(self,col_name,value,id):
        sql = "update students set {} = '{}' where studentNo = {}".format(col_name,value,id)
        result = self.mysql.update(sql)
        if not result:
            print("修改学生信息成功")
        else:
            print("修改学生信息失败")



    #查询学生的业务

    def get_student(self,name):
        sql = "select * from students where name like '%{}%'".format(name)
        result = self.mysql.get_all(sql)
        if result:
            print("查询结果成功:{}".format(result))
        else:
            print("查询失败")


if __name__ == "__main__":
    s = Student()
    #s.get_student("刘邦")
    #s.add_student('14','张三',42,'女','6班','1101234566','上海')
    #s.add_student('15','李四','30','女','6班')
    #s.mod_student('age','38',9)
    #s.mox_student(15)