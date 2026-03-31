import sys

class Customer:

    bank_name = "STATE BANK OF INDIA"

    def __init__(self, name):
        self.name = name
        self.balance = 1000

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited Successfully")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient Funds")
            sys.exit()

        self.balance = self.balance - amount
        print("Amount Withdrawn Successfully")
        print("Current Balance:", self.balance)


print("Welcome to", Customer.bank_name)

name = input("Enter your name to create account: ")

customer1 = Customer(name)

print("Account created successfully")
print("Default Balance =", customer1.balance)


while True:

    print("\n---- Banking Menu ---- \n \t1. Deposit Money \n \t2. Withdraw Money \n \t3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        amount = int(input("Enter amount to deposit: "))
        customer1.deposit(amount)

    elif choice == "2":

        amount = int(input("Enter amount to withdraw: "))
        customer1.withdraw(amount)

    elif choice == "3":

        print("Thank you for using SBI Banking")
        sys.exit()

    else:

        print("Invalid Choice. Please select a valid option.")