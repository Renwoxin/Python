# 注意： 在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数
# 都能够正常的访问到每一个全局变量
gl_num = 10

# 再定义一个全局变量
gl_title = "黑狗程序员"

# 再定义一个全局变量
gl_name = "xm"


def demo():
    # 如果局部全局变量的名字和全局变量的名字相同
    # PyCharm会在局部变量下方显示一个灰色的虚线
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)

demo()