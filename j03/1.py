f1 = 1
f2 = 1

n = int(input("enter a number: "))

if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
else:
    print(f1, f2, end=" ")
    i = 3
    while i <= n:
        f1, f2 = f2, f1 + f2
        print(f2, end=" ")
        i += 1