class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __move(self):
        print('I am moving')
    
    def __str__(self):
        return f'Person: {self.name}, {self.age}'


p = Person('John', 30) # p is an instance of Person
p.__move()  # AttributeError: 'Person' object has no attribute '__move'
p.__str__()  # AttributeError: 'Person' object has no attribute '__str__'