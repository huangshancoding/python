# 全局变量 global语句
# 在编写程序的时候，如果想为一个在函数外的变量重新赋值，并且这个变量会作用于许多函数中时，
# 就需要告诉python这个变量的作用域是全局变量。
# 此时用global语句就可以变成这个任务，也就是说没有用global语句的情况下，是不能修改全局变量的。

a = 6
def func_global():
    global a #a为全局变量,声明多个变量的格式为 global a,b,c
    print("a = ", a) #6
    a = 2
    print("a = ",a) #2
func_global() # 调用函数
print("a = ",a) #2

#在另外一个函数在调用一次a ，变化a 的值看是否有变化
def func_2():
    # global a
    a = 7
    print("a = ",a)
func_2()
print("a = ",a)