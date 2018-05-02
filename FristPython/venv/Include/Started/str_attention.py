#一些字符串的注意事项

#print总是会以一个不可见的"新一行"字符(/n)结尾，因此print总是会换行，为了防止这种换行符，可以通过end指定其应以空白结尾;
print('a',end='')
print('b')

#或者end=任意字符，即以该字符结尾
print('a',end=' ')
print('b',end='$')
print('c')

#转义序列 \,多的就不说了，其他语言学过的，其实是一样的
print('what\'s your name?')#等同于
print("what's your name?")
#一个放在末尾的反斜杠\表示字符串将在下一行继续，但是不会添加新的一行。
print("我叫刘祥龙。\
我正在学python")#等同于
print("我叫刘祥龙。我正在学习python")
#显示行链接
s='This is a string.' \
  'This is the String'
print(s)