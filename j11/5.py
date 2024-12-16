class Alive:
    def move(self):
        pass

class Person(Alive):
    def __init__(self, name):
        self.name = name
    def move(self, name):
        print(name ,"is walking...")

class Dog(Alive):
    def move(self):
        print("Dog is running...")

class Fish(Alive):
    def move(self):
        print("Fish is swimming...")

p1 = Person("ali")
p1.move("ali")

p2 = Person("reza")
p2.move("reza")

d1 = Dog()
d1.move()

f1 = Fish()
f1.move()