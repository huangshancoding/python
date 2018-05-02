import os
import time

# 基于windows下的压缩备份 01版本

# 要保存的文件
source = ['"E:\\test01"']
# 目标目录
target_dir = 'E:\\TestPython'
# 备份文件将打包压缩为zip文件
# zip压缩文件的文件名由当前日期和时间构成
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

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