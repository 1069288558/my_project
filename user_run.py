

from controller.student import Student


if __name__ == '__main__':
    text = input("请输入数据:")
    #判断text ,1
    """
       1.当用户传入的值是1或者是'新增' ,就给他调用新增。 继续传入新增所需要的参数
       2.当用户传入的值是2或者'修改'，就给他调用修改方法，继续传入修改参数
       3.当用户传入的是3或者'删除'，就给他调用删除的方法，继续传入删除的参数
       4.否则，就调用查询方法
    """
    st = Student()
    text = input("请输入数据:")
    if text in ['1','新增']:
        print("开始调用新增的方法")
        add = input()
        lst = add.split(" ")
        st.add_student(*lst)
    elif text in ['2','修改']:
        print("开始调用修改方法")
    elif text in ['3','删除']:
        print("开始调用删除方法")
    else:
        print("开始调用查询方法")
        name = input()
        st.get_student(name)