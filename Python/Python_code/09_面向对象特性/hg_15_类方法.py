class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)
    def __init__(self, name):

        self.name = name

        Tool.count += 1


tool1 = Tool("futou")
tool2 = Tool("langtou")

Tool.show_tool_count()