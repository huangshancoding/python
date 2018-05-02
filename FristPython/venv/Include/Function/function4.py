#默认参数值 在函数定义时附加一个赋值运算符(=)来为参数指定默认参数值
#注意默认参数值是常量，不可变的
def say(message,times = 1):
    print(message * times)

say("hello")
say("jack",5)

#再来一个比较复杂点的 关键字参数
def func(a,b = 10,c = 20):
    print("a is",a,"and b is",b,"and c is",c)
func(3,5)
func(12, c=40)
func(c = 50, a = 100)

# 再来一个 可变参数,想在函数里定义任意数量的变量，也就是说参数数量是可变的，可以通过星号实现
def total(a = 5,*numbers,**phonebook):#当我们声明一个 *param的星号的参数时，
    # 从此处开始直到结束的所有位置参数都将被收集汇集成一个称为“param”的元祖(Tuple)
    # 当我们声明一个诸如 **param的双星号参数时，从此处开始直到结束的所有位置参数都将被收集汇集成一个称为“param”的字典(Dictionary)
    print("a",a)
    # 遍历元祖中的所有项目
    for single_item in numbers:
        print("single_item",single_item)
    # 遍历字典中所有的项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,4,5,Jack=1111,John=2222,Mark=3333))
