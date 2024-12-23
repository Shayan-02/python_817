class Person:
    def __init__(self, name, age):
        """
        Initialize a Person object with given name and age.
        :param name: name of the person
        :param age: age of the person
        :type name: str
        :type age: int
        """
        self.name = name
        self.age = age
    
    def move(self):
        pass

class Student(Person):
    def move(self):
        print("Student is walking...")


class Baby(Person):
    def move(self, movement):
        print(f"{self.name} is {movement}ing...")

s1 = Student("ali", 15)
s1.move()
b1 = Baby(name="reza", age=1)
b1.move("crawl")
