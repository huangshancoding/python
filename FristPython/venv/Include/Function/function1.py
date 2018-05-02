# coding=utf-8
#函数的基本样式
def say_hello():
    #该块属于这一函数
    print("hello world")
#函数结束

say_hello() #调用函数
say_hello() #再次调用函数


#有参数的函数
def print_max(a,b):
    if a>b:
        print("a更加大!")
    elif a == b:
        print("两者相等!")
    else:
        print("b更大!")
print_max(2,5) #调用函数
