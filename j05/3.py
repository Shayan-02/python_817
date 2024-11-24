ali_rezaee = {
    "fname": "ali",
    "lname": "rezaee",
    "age": 30,
    "gpa": 19.5,
    "major": "کامپیوتر",
}

ali_rezaee["gpa"] = 20

# ali_rezaee["phone"] = "0987654321"

ali_rezaee.update({"phone": "0987654321"})
ali_rezaee.update({"age": 31})

ali_rezaee.pop("gpa")
ali_rezaee.popitem()
# ali_rezaee.clear()
print(ali_rezaee)


print(ali_rezaee.get("age"))
print(ali_rezaee.get("fname"))
print(ali_rezaee["fname"])
