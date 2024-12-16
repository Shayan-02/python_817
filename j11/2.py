class Person:
    def __init__(self, name, pid, age):
        self.esm = name
        self.pid = pid
        self.age = age


p1 = Person("ali", 1, 30)
print(p1.esm)
b = p1.age