thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
ali_rezaee = {
    "fname": "ali",
    "lname": "rezaee",
    "age": 30,
    "gpa": 19.5,
    "major": "کامپیوتر"
}

# print(thisdict)
# print(ali_rezaee)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

for i in thisdict.items():
    print(i, end=" ")

print()
print("******************************")
for i in ali_rezaee:
    print(f"{i}: {ali_rezaee[i]}")

for i in ali_rezaee:
    print(i, ali_rezaee[i], end="\n")
    