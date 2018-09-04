# 使用多个键值对，存储描述一个物体的相关信息——描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历
card_list = [
    {"name":"小明",
     "qq":"111111",
     "phone":"10086"},
    {"name":"lisi",
     "qq":"222222",
     "phone":"2222"}
]

for card_info in card_list:
    print(card_info)