# 1.定义holiday_name 字符串变量记录节日名称
holiday_name = "情人节"
# 如果是情人节 应该买玫瑰/看电影
if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
# 如果是平安夜应该买苹果/吃大餐
elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")
# 如果是生日 应该买蛋糕
elif holiday_name == "生日":
    print("买蛋糕")
# 其他每天都是节日
else:
    print("其他每天都是节日")