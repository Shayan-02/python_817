lst = [1, 1, 2, 1, 1, 4, 2, 3, 3, 1, 1, 2, "ali"]
# lst.clear()
c = lst.copy()
print(lst == c)
lst.append("2")
c.append("1")
print(c)
b = ["ali", "reza", "mohammad"]

print("lst", lst)
b.sort()
lst.reverse()
print("reverse", lst)