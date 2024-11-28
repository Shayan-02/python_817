lst = []
for i in range(1, 4001):
    lst.append(str(i))
    a = "".join(lst)

n = int(input())
print(a[n-1])