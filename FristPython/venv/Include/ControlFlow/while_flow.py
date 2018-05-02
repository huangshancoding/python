number = 23
running = True

while running:
    input_num = int(input("请输入一个数字:"))

    if number == input_num:
        print("恭喜你答对了!")
        running = False
    elif input_num < number:
        print("太小了！")
    else:
        print("太大了!")
else:
    print("恭喜你获得一个范冰冰的亲吻！")

print("爽死你!")