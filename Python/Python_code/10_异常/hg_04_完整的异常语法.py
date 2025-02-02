try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 使用8除以用户输入的整数并且输出
    result = 8/num

    print(result)

except ValueError:
    print("未输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行的代码")

print("-" * 50)