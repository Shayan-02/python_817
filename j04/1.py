fname = "ali"
lname = "rezaee"
age = 30
gpa = 19.5
major = "کامپیوتر"
print(len(fname))
ali_rezaee = [fname, lname, age, gpa, major]
print(ali_rezaee)

for _ in ali_rezaee:
    if type(_) == float:
        print(_) 
        