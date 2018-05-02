import os
import time

# 要保存的文件
source = ['"E:\\test01"']
# 目标目录
target_dir = 'E:\\TestPython'

# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 将当前日期作为主备份目录下的子目录名称
today = target_dir+"\\"+ time.strftime('%Y%m%d')
# 将当前日期作为zip 文件的文件名
now = time.strftime('%H%M%S')

# 添加一条来自用户的注释以创建
comment = input("请输入注释:")
# 检查是否有评论键入
if len(comment) == 0:
    target  = today+ os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print("成功创建文件夹")

# 我们使用zip命令将文件打包成zip格式
zip_commond = 'HaoZipC a -tzip {0} {1}'.format(target,' '.join(source))

# 运行备份
print('HaoZip command is:')
print(zip_commond)
print("Running:")
if os.system(zip_commond) == 0:
    print("压缩完成,文件为: ",target)
else:
    print("压缩失败")