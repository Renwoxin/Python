xiaoming_dict = {"name":"小明"}

# 1.取值
print(xiaoming_dict["name"])
# 在取值时，如果指定的key不存在，程序会报错
# print(xiaoming_dict["name123"])

# 2.增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在。会修改已近存在的键值对
xiaoming_dict["name"] = "xxm"
# 3.删除
xiaoming_dict.pop("name")
# 再删除指定键值时，如果指定键值key不存在，程序会报错
# xiaoming_dict.pop("name123")
print(xiaoming_dict)