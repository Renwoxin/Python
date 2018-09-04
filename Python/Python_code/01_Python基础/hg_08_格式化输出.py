# 定义字符串变量 name， 输出 请多多关照
name = "小明"
print("%s,请多多关照"%name)
# 定义整数变量std_no,输出 学号 000001
std_no = 1
print("学号 %06d"%std_no)
# 定义小数price、weight、money，
# 输出 苹果单价，购买了5，需要支付45
price = 8.5
weight = 7.5
money = price * weight
# print("苹果单价 %f，购买了 %f，需要支付 %f" % (price,weight,money))
#苹果单价 8.500000，购买了 7.500000，需要支付 63.750000
print("苹果单价 %.2f，购买了 %.3f，需要支付 %.4f" % (price,weight,money))
#苹果单价 8.50，购买了 7.500，需要支付 63.7500
# 定义一个小数scale, 输出 数据比例是 10.00%
scale = 0.25 * 100
# print("数据比例是 %f%%" %scale)
# 数据比例是 25.000000%
print("数据比例是 %.2f%%" %scale)
# 数据比例是 25.00%