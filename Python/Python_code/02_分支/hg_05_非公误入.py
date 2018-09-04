# 定义一个布尔型变量is_employee,编写判断是否是本公司员工
is_employee = False
# 如果不是提示不允许入内
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# 如果需要拼接复杂的逻辑计算条件，同样也可能使用到not
if not is_employee:
    print("非本公司人员，不得入内")
