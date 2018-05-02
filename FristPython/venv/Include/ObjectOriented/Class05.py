# 继承，面向对象几大特征之一哦
class SchoolMember:
    """代表任何学校里的成员"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("初始化学校成员,名字为:{}".format(self.name))

    def tell(self):
        """告诉我有关于我的细节"""
        print("姓名:'{}',年龄:'{}'".format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    """代表一位老师"""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age) #在java中相当于super(),python中不会自动调用基类SchoolMemeber的构造函数
                                             # 自己必须显示的调用它
        self.salary = salary
        print("初始化老师,名字为:{}".format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("薪水:'{:d}'".format(self.salary))

class Student(SchoolMember):
    """代表一位学生"""
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("初始化学生，名字为:{}".format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("分数为:'{:d}'".format(self.marks))

t = Teacher("马云",53,30000)
s = Student("刘祥龙",25,100)
print("-----------")
members = [t,s]
for member in members:
    member.tell()
