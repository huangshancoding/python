#if 语句
number = 23
input_num = int(input('请输入一个数字： '))

if number == input_num:
    print('恭喜你，猜对了！')
    print('但是并没什么卵用。。。。。')
elif input_num < number:
    print("你猜的太小了！")
else:
    print("你猜的太大了！")

if True:
    print("我很帅")