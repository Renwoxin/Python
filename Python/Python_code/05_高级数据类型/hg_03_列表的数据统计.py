# 定义一个列表
name_list = ["zhangsan","lisi","wangwu"]
list_len = len(name_list)
print("列表中包含的%d个元素" % list_len)

# count方法可以统计列表中某一个数据出现的次数
count = name_list.count("lisi")
print("lisi出现了%d次" % count)
# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("lisi")
print(name_list)