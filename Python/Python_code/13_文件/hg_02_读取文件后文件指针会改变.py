# 1.打开文件
file = open("README")

# 2.读取文件
text = file.read()
print(text)
print(len(text))
print("-" * 50)

# read 方法执行之后，文件指针会移动到
# 文件末尾，之后就不能读取数据了
text = file.read()
print(text)
# 3.关闭文件
file.close()