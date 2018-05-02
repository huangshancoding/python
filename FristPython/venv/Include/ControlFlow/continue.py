while True:
    s = input("请输入：")
    if s == "退出":
        break
    elif len(s) != 15:
        print("长度不符合,你输入的长度为",len(s))
        continue
    print("长度符合!")
