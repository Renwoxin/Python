a = 6
b = 99

# 解法1： 使用其他变量
# c = a
# a = b
# b = c
# 解法2：不使用其他变量
# a = a + b
# b = a - b
# a = a - b
# 解法3：Python专有
# a,b = (b,a)
# 等号右边是元组，只是把小括号省略了
a,b = b,a
print(a)
print(b)