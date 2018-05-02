# 局部变量 变量只存在于函数这一局部 例如
x = 25
def func(x):
    print("x = ",x)
    x = 100 #局部变量
    print("x = ",x)
func(x) #调用函数
print("x = ",x) #x并没有变化

