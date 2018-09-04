# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具!

def say_hello():
    print("xmeihfe")

# 如果直接执行模块，始终输出__main__,以下代码不会被导入
if __name__ == "__main__":

    print(__name__)

    print("xmkaifademokuai")
    say_hello()