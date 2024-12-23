class BankAccount:
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.05):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {
                      self.balance:}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print(f"Account Number: {self.account_number}\nAccount Owner: {self.owner_name}\nAccount Owner: {self.owner_name}")


# Using the BankAccount class
account1 = BankAccount("1234567890", "John Smith")
account1.deposit(1000)
account1.withdraw(500)
account1.display_info()

account2 = BankAccount("9876543210", "Jane Doe", interest_rate=0.1)
account2.deposit(1500)
account2.withdraw(3000)
account2.display_info()
