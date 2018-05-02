#在python中字符串是不可变的
#python 字符串format方法
age = 25
name = '刘祥龙'
print('{0}的年龄是{1}'.format(name,age))
print('{0}正在学python'.format(name))
#其中的数字是可以省略的
print('{}的年龄是{}'.format(name,age))
print('{}正在学python'.format(name))

#也可以使用下面的方法实现,但是不推荐使用，比较丑陋
msg = name + '的年龄是' +str(age)
print(msg)

#format方法所做的的事情便是将每个参数数值替换至格式所在的位置。这其中可以有更详细的格式，例如
print('{0:.3f}'.format(1.0/3))#对浮点数"0.33333..."保留小数点.后三位
print('{0:_^11}'.format('hello'))# 1）使用下划线填充文本，并保持文字处于中间位置；2)使用^定义'___hello___'字符串长度为11
print('{name}正在学习python,年龄为{age}'.format(name="刘祥龙",age=25))