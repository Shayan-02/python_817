class Dog:
    # Class variable
    s = "C"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def bark(self, name):
        print(name, "Woof!")


# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.s)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)  # (Instance variable)

# Call methods
dog1.bark("Buddy")

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.s = "Feline"
print(dog1.s)  # (Updated class variable)
print(dog2.s)
