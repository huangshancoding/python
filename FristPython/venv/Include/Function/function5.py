#return 语句的使用
def maximun(x,y):
    if x > y:
        return x
    elif x == y:
        return "两个数相等"
    else:
        return y
print(maximun(2,3))

# 示例2 每个函数都在其末尾 隐含了一句return None,除非你写了你自己的return语句。
def some_function():
    pass #python 中的 pass 语句用于指示一个没有内容的语句块