# 定义一个列表
name_list = ["zhangsan","lisi","wangwu"]
# 使用del关键字（delete）删除列元素
# 提示：在日常开发中，要从列表中删除数据，建议使用列表提供的方法
del name_list[1]

# del关键字本质上是用来将一个变量从内存中删除
name = "小明"
del name
print(name)
print(name_list)
