import random
# 不能和系统模块重名

# __file__ 查看模块导入路径
print(random.__file__)

rand = random.randint(0,10)

print(rand)