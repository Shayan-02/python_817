
num1 = int(input("enter first number: "))
op = input("enter operator: ")
num2 = int(input("enter second number: "))

try:
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("invalid operator")
# except ZeroDivisionError:
#     print("zero division error")
except Exception as e:
    print(e)
print("end")