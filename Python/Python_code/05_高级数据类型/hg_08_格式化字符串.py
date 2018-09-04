info_tuple = ("lisi",18,1.786)
# 格式化字符串后面 ’（）‘本质上就是元组
print("%s %d %f" % ("lisi",20,1.786))
print("%s %d %f" % info_tuple)
info_str = "%s %d %f" % info_tuple
print(info_str)