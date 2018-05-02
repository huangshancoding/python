# __init__方法 在类的对象被实例化的时候立即执行。这一方法可以对任何你想进行操作的目标对象进行初始化操作，
# JAVA中构造器了解下？
class Person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print("Hello! My Name is",self.name)
p = Person("刘祥龙")
p.say_hi()