# 1. 判断空白字符
space_str = " \t\r\n"
print(space_str.isspace())
# 2. 判断字符串中是否只包含数字
# 1> 以下三个方法都不能判断小数
# num_str = "1"
# 2> unicode字符串
# num_str = "\u00b2"
# num_str = "（1）"
# 3> 中文数字
num_str = "一千零一夜"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())  # ——可是我自己的结果是 False