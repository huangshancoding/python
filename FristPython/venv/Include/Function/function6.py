#DocString 函数在第一行逻辑行中的字符串是该函数的文档字符串（DocString）
# 在程序运行时，通过函数的__doc__属性来获取文档
def print_max(x,y):
    '''打印两个数值中最大的数，
    这两个数应该都是整数'''
    x = int(x)
    y = int(y)

    if x > y:
        print("x更大")
    elif x == y:
        print("两者相等")
    else:
        print("y更大")
print_max(13,15)
print(print_max.__doc__)