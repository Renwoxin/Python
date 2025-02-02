class Musicplayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:

            # 2. 调用父类的方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)

        return cls.instance
    
    pass

# 创建多个对象
player1 = Musicplayer()
print(player1)

player2 = Musicplayer()
print(player2)