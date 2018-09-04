def multiple_table():

    # 打印9行小星星
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*",end="")
            print("%d * %d = %d" %(col,row,col * row), end="\t")
            col += 1
        print("")  # 在一行输出完成之后，添加换行
        row += 1
