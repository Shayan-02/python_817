class Test:
    def sayName(self, __name):
        return __name

t1 = Test()
t1.sayName("alireza")
print("t1:", t1.sayName("alireza"))

t2 = Test()
print("t2:", t2.sayName("mohammad"))

