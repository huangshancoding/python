# from..import  如果你希望直接将argv变量导入你的程序(为了避免每次都要输入 sys.),
# 那么你可以通过使用 from sys import argv 语句来实现这一点

##### 警告：一般来说，你应该尽量避免使用 from...import语句，而去使用import语句。
##### 这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。
from math import sqrt
print("Square root of 16 is",sqrt(16))

if __name__ == "__main__": #每个Python模块都定义了它的__name__属性。如果它与__main__属性相同则代表这一模块是由用户独立运行的。
    print("this is being run by itself") #在本模块运行时你会发现 输出的是这句话
else:
    print("I am being imported from another module") #在modules01 模块导入本模块，你会发现modules01会输入这句话