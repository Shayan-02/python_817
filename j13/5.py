valid = [10**x for x in range(0, 101)]
n1 = int(input("enter number1: "))
op = input("enter op: ")
n2 = int(input("enter number2: "))
if n1 in valid and n2 in valid:
    if op == "+":
        print(n1 + n2)
    elif op == "*":
        print(n1 * n2)
