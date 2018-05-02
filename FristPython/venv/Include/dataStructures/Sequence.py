# 序列Sequence
# 列表，元祖和字符串都可以看做序列(Sequence)的某种表现形式。
# 序列的主要功能是资格测试(MembershipTest) (也就是in 与 not in表达式) 和索引操作(Indexing Operations)
# 它们能够允许我们直接获取序列中的特定项目，前面学的列表，元祖和字符串同样拥有切片(Slicing)运算符

shoplist = ["apple","mango","carrot","banana"]
name = "LXL"

print("第一个水果为：",shoplist[0])
print("第二个水果为：",shoplist[1])
print("第三个水果为：",shoplist[2])
print("第四个水果为：",shoplist[3])
print("倒数第一个水果为：",shoplist[-1])
print("倒数第二个水果为：",shoplist[-2])
print("第一个字符为:",name[0])

#切片操作 含头不含尾
print("下标1到3的水果为:",shoplist[1:3])
print("下标1到最后的水果为：",shoplist[1:])
print("下标为1到-1的水果为：",shoplist[1:-1])
print("从头到尾的名字为:",name[:])

# 同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长(step)
print(shoplist[::1])# 步长为1
print(shoplist[::2])# 步长为2 取0,2,4等，2的倍数
print(shoplist[::3])# 步长为3 取3的倍数，0,3,6,9
print(shoplist[::4])# 步长为4 取4的倍数，0,4,8
print(shoplist[::-1])# 步长为-1 从后往前取相应的步长
