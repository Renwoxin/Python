# 1.打开文件
file_read = open("README")
file_write = open("README[copy]", "w")
# 2.读、写
text = file_read.read()
file_write.write(text)
# 3.关闭
file_write.close()
file_read.close()