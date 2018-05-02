# 元祖(Tuple)用于将多个对象保存在一起。你可以将它们近似的看做是列表，但是元祖不能提供列表类给你的广泛功能。
# 元祖的一大特征类似于字符串，他们是不可变的，也就是说，你不能编辑或更改元祖。
# 元祖通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，意即元祖内的数值不会改变

# 元祖壳使用括号，也可不使用括号，但是我推荐使用括号来表明元祖的开始和结束
zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))

new_zoo = 'monkey','camel',zoo
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2]) #下标从0开始
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))# new_zoo 前两个数加zoo的数

# 0个项目的元祖，一个空的元祖由一对圆括号构成。
empty = ()
print(empty)
print(type(empty))

# 1个项目的元祖，必须在括号内该项目后加个逗号(,)，否则指定的是其他的对象，如下
zoo2 = (1)
print(type(zoo2)) #int
zoo3 = (1,)
print(type(zoo3)) #tuple