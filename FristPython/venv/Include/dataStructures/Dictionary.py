# 字典 dictionary   {key:value,key:value},类似 java中的json对象,
# 字典的key只能是不可变的对象（如字符串）
# 字典中的成对的键值与值得配对不会以任何方式进行排序。

ab = {
    "liudehua":"liudehua@qq.com",
    "zhangxueyou":"zhangxueyou@qq.com",
    "zhoujielun":"zhoujielun@qq.com",
    "liuxianglong":"liuxianglong@qq.com"
}

print("liudehua's address is",ab['liudehua'])

#删除一对键值对配对
del ab["zhangxueyou"]
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print("{}'s address is {}".format(name,address))

#添加一对键值 - 值配对
ab['linjunjie'] = "linjunjie@qq.com"
if "linjunjie" in ab:
    print("\nlinjunjue's adress is", ab["linjunjie"])