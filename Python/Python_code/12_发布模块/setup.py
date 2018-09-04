from distutils.core import setup

setup(name="hg_message", # 包名
      version="1.0", # 版本
      description="hg发送和接收消息模块", # 描述信息
      long_description="完整的发送和接收消息模块", # 完整的描述信息
      author="hg", # 作者
      author_email="666666@qq.com", # 作者邮箱
      url="www.hg.com", # 主页
      py_modules = ["hg_message.send_message",
                    "hg_message.receive_message"])