for i in range(1, 10):
    if i == 6:
        continue
    print(i, end=" ")

print()

i = 1
while i <= 10:
    if i == 6:
        i += 2
        continue
    if i == 9:
        break
    print(i, end=" ")
    i += 1