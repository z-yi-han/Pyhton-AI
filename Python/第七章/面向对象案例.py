class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学：{self.math}|英语:{self.english} "

    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生成绩
    def add_student(self):  # 移除了student参数
        name = input("输入学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在,添加失败")
                return
        chinese = int(input("输入学生语文成绩: "))
        math = int(input("输入学生数学成绩: "))
        english = int(input("输入学生英语成绩: "))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生成绩输入错误")

    # 修改学生成绩
    def update_student(self):
        name = input("输入学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩是:{s}")
                print("请输入修改后的成绩")
                chinese = int(input("输入学生语文成绩: "))
                math = int(input("输入学生数学成绩: "))
                english = int(input("输入学生英语成绩: "))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("学生成绩输入错误")
                    return
        print("未找到该学生,修改失败")

    # 删除学生成绩
    def delete_student(self):
        name = input("输入学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败")
    #查询学生成绩
    def query_student(self):
        name = input("输入学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"学生西南西: {s}")
                return
        print("未找到学生")
    # 显示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
        while True:
            print()
            print("###############################################################")
            print("1.添加学生 2,修改学生 3，删除学生 4.查询指定学生 5.查询所有学生 6.退出系统")
            print("###############################################################")
            print()
            choice = input("请选择操作，输入1-6：")
            match choice:
                case "1":
                    self.add_student()  # 不需要传参
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    # 这里可以添加查询指定学生的功能
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    print("Bye~")
                    break
                case _:
                    print("输入错误,请重新输入")


if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()
