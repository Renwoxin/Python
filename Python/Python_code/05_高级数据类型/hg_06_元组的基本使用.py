info_tuple = ("lisi",18,1.786)
# 1.取值和去索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("lisi"))
# 2.统计数据
print(info_tuple.count("lisi"))
# 统计元组中包含元素的个数
print(len(info_tuple))