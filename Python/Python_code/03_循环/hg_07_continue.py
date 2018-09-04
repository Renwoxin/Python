i = 0
while i < 10:

    # continue 某一条件满足时，不再执行后续重复的代码
    # i == 3
    if i == 3:
        # 注意：在循环中，如果使用continue这个关键字
        # 在使用关键字之前，需要确认循环计数是否修改
        #否则会导致死循环
        i += 1
        continue
    print(i)
    i += 1
