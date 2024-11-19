lst = ["alireza", "ali", "reza", "mohammad"]

lst.append(3)
lst.append(4)
lst.append(5)
lst.insert(3, "ali")
print(lst)

sum = 0
for _ in lst[0:3]:
    sum += len(_)
print(sum)