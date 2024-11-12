num1 = 10
num2 = 20
num3 = 30

if num1 > num2 < num3:
    print("min is: ", num1)
elif num2 < num1 and num2 < num3:
    print("min is: ", num2)
elif num1 > num2 or num2 == 20:
    print("min is: ", num3)