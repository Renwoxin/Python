def demo(num,num_list):

    print("函数开始")

    # num = num + num
    num += num  # 属于正常的变量赋值类型，会修改变量的引用

    # num_list = num_list + num_list
    # num_list.extend(num_list)由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    # num_list += num_list
    print(num)
    print(num_list)
    print("函数完成")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)