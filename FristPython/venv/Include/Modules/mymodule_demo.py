
#导入 mymodule模块
#第一种写法
# import mymodule
#
# mymodule.say_hi()
# print('Version',mymodule.__version__)

# 第二种写法
from mymodule import say_hi,__version__
say_hi()
print('Version',__version__)

# 第三种写法 from mymodule import*
# 这样导入诸如 say_hi 等所有公共名称，但是不会导入 __version__名称，因为后者以双下划线开头。以__开头的代表私有成员