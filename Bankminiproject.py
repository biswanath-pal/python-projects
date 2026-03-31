class Customer:

    """Customer class"""

    bank_name="STATE BANK OF INDIA"

    def __init__(self,name):
        self.name=name
        self.balance=1000

    def checkbalance(self):
        print(f"Balance in your account: {self.balance}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Successful")
        print("Your Current Balance is: ",self.balance)

    def withdraw(self,amount):

        if amount <= self.balance:

            self.balance = self.balance - amount
            print("Your withdraw request completed successfully")
            print("Available Balance: ",self.balance)

        else:

            print("You have insufficient Balance in you account")


def option():
    
    choice=int(input("\tBanking Menu\t \n\t 1.deposit \n\t 2.withraw \n\t 3.checkbalance \n\t 4.Exit \n"))

    if choice == 1:

        amount=int(input("Enter amount to deposit: "))
        c.deposit(amount)
        option()

    elif choice == 2:

        amount=int(input("Enter amount to withdraw:"))
        c.withdraw(amount)
        option()

    elif choice == 3:

        c.checkbalance()
        option()

    elif choice == 4:

        print("Thank you for using SBI Banking")

    else:

        print("'Invalid' \n Please select a Valid option")   
        option()       

print("Welcome to ",Customer.bank_name)       
name=input("Enter Customer Name: ")
c=Customer(name)
print("Account Created Successfully \n Default Balance=",c.balance)
option()