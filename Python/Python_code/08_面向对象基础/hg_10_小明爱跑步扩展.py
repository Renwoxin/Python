class Person:
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "my name is %s weight is %.2f" % (self.name,self.weight)

    def run(self):
        print("%s 爱跑步" % self.name)

    def eat(self):
        print("%s 是吃货" % self.name)
        self.weight += 1

xm = Person("xm",75.0)

xm.run()
xm.eat()

print(xm)

xmei = Person("xmei",75.0)

xmei.run()
xmei.eat()

print(xmei)
print(xm)