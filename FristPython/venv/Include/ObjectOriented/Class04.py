# 类变量和对象变量
# 类变量：是可以被共享的，它们可以被属于该类的所有实例访问。该类变量值拥有一个副本，
# 当任何一个对象对类变量做改变时，发生的变动将在其他所有实例中得到体现。
# 对象变量：由类的每一个独立对象或实例所拥有。在这种情况，每个对象都拥有属于它自己的字段的副本，也就是说，他们不会被共享，
# 不会以任何方式与其它不同实例中的相同字段产生关联。
class Robot:
    """表示有一个带有名字的机器人。"""
    # 一个类变量，用来计数机器人的数量
    population = 0
    def __init__(self,name): #name 就是对象变量
        """初始化数据"""
        self.name = name
        print("初始化{}".format(self.name))

        # #当有人被创建的时候，机器人口将会加1
        # Robot.population += 1
        self.__class__.population +=1             # 调用类变量时还可以用self.__class__.population
    def die(self):
        """我挂了"""
        print("{}正在被销毁".format(self.name))
        Robot.population -=1
        if Robot.population == 0:
            print("{} 是最后一个了".format(self.name))
        else:
            print("这依然有{:d}机器人在工作".format(Robot.population))
    def say_hi(self):
        """来自机器人的问候"""
        print("大家好，我的主人叫我{}".format(self.name))

    @classmethod #这表明how_many方法是一个属于类并非属于对象的方法，也就是静态方法，所以也可以定义为staticmethod,
                 # 但是如果使用 staticmethod 调用时需要传入类名
                 # @classmethod --- 装饰器,启用装饰器等价于 how_many = classmethod(how_many)
    def how_many(cls):
        """打印除当前的人口数量"""
        print("我们有{:d}个机器人".format(cls.population))

robot1 = Robot("一号机器人")
robot1.say_hi()
# Robot.how_many(Robot)
Robot.how_many()
robot2 = Robot("二号机器人")
robot2.say_hi()
# Robot.how_many(Robot)
Robot.how_many()

robot1.die()
robot2.die()
# Robot.how_many(Robot)
Robot.how_many()

# 输出类文档信息
print(Robot.__doc__)
# 输出方法文档信息
print(Robot.say_hi.__doc__)
print(Robot.how_many.__doc__) #注意python 以下划线开头的变量，那么这个变量即为私有变量，前面说过的