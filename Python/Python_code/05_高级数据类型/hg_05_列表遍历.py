name_list = ["zhangsan","lisi","wangwu","wangxiaoer"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在my_name
变量中，在循环体内部可以访问到当前这一次获取到的数据
"""
for my_name in name_list:
    print("my name is %s" % my_name)
