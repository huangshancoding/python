import sys #sys 模块包含了与Python解释器及其环境相关的功能，也就是所谓的系统功能
# import modules02

print("The command line arguments are:")

for i in sys.argv:
    print(i)

print('\n\nThe PythonPath is ',sys.path)

