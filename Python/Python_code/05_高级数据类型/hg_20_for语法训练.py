for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用了break退出循
    # 环，else下方代码不会被执行
    print("what")
print("循环结束")