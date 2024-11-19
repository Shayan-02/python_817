lst = ["alireza", "reza", "ali", "reza", "mohammad", "reza"]

for _ in lst:
    if _ == "reza":
        lst.remove(_)

print(lst)

choices = ["rock", "paper", "scissors"]
user_choice = input("enter your choice: ")

if user_choice in choices:
    print("valid choice")
else:
    print("invalid choice")