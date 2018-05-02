# 有关字符串的更多内容
# 这是一个字符串
name = "LiuXiangLong"

if name.startswith('Liu'):
    print("Yes")
if 'X' in name:
    print("Yes")
if name.find('Long'):
    print("Yes")

delimiter = '*'
mylist = ['one','two','three']
print(delimiter.join(mylist))