def mahal(a:str):
    if a[0] == a[2]:
        return "Vertical"
    elif a[1] == a[3]:
        return "Horizontal"
    else:
        return "Try again"

adress = input().split()
print(mahal(adress))