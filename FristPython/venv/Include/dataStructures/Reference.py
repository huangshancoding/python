# 对象的引用  学过面向对象的语言的对这个肯定比较了解如JAVA
# 当你创建了一个对象并分配给某个变量时，变量只会查阅某个对象，并且它不会代表对象本身。
# 也就是说，变量名只是指向你计算机内存中存储了相应对象的那一部分。这叫做将名称绑定给那一个对象。
shoplist = ['apple','mango','carrot','banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
del shoplist[0]
print("shoplist is",shoplist)
print("mylist is",mylist) #两个列表结果一样


#但是如果我现在换种写法
mylist01 = shoplist[:]
del mylist01[0]
print("shoplist is",shoplist)
print("mylist01 is",mylist01) #发现两个列表是不同的