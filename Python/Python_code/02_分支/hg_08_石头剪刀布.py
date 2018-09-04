# 导入随机工具包
# 注意：在导入工具包时，应该将导入的语句放在文件的顶部
# 方便下方代码使用
import random
# 从控制台输入拳 ——石头（1）/剪刀（2）/布（3）
player = int(input("请输入出拳 石头（1）/剪刀（2）/布（3）:"))
# 电脑随机出拳——先假定电脑只会出石头（1）
computer = random.randint(1,3)
print("玩家选择拳头%d-电脑出拳%d" % (player,computer))
# 比较胜负
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
# if (()
# or ()
# or ()): ——调整代码格式，方便阅读
if ((player == 1 and computer == 2)
        or(player == 2 and computer == 3)
        or(player == 3 and computer ==1)):

    print("人类完爆了")
# 平局
elif player == computer:
    print("平局")
# 其他的情况都是电脑获胜
else:
    print("电脑获胜")
