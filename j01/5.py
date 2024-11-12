fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))

print(f"Hello, {fname} {lname} you are {age} years old")
print("Hello, {} {} you are {} years old".format(lname, fname, age))
