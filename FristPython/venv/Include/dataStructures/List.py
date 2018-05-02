#list  可变的，可保存有序项目的集合
shopList =  ['apple','mango','carrot','banana']
print('我有',len(shopList),'商品去买')
print('这些商品为：',end=' ')
for item in shopList:
    print(item,end= ' ')
print('\n我还要去买米')
shopList.append('rice')
print('我现在买好的东西为:',shopList)

print("我要开始排序了")
shopList.sort()
print("排序好的商品为：",shopList)

print("我要买的第一个商品为: ",shopList[0])
olditem = shopList[0]
del shopList[0] #del 是python中的删除
print("我买好了",olditem)
print("我现在的商品列表为:",shopList)