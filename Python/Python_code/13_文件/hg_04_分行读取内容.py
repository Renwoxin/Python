file = open("README")

while True:
    txt = file.readline()

    # 判断是否读取到内容
    if not txt:
        break
    print(txt)

file.close()