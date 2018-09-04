student = [
    {"name":"阿猫"},
    {"name":"阿狗"}
]

find_name = "阿猫"
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望统一的提示！
    print("没有找到 %s" % find_name)
print("循环结束")