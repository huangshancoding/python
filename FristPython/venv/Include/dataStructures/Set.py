# 集合（Set）是简单对象的无序集合（Collection）。以大括号表示{}
# 通过使用集合，可以测试某些对象的资格或者情况，检查它们是否是其他集合的子集，找到两个集合的交集，等等。
country = ['brazil','russia','india']
bri = set(country)
print(bri)
print(type(bri))

country01 = {'brazil','russia','india'}
bri01 = set(country01)
print(bri01)
print(type(bri01))


# set一些方法
bri_copy = bri.copy()
bri_copy.add('china')
print(bri_copy.issuperset(bri)) #issuperset 判断前一个是否是后一个超集 就是后一个是前一个的真子集

bri.remove('russia')
print(bri & bri_copy)