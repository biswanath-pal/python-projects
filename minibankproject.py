class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount} to {self.name}.")

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return True  # Success
        else:
            print(f"Transfer Failed: {self.name} has insufficient funds!")
            return False  # Failure

    # Transfer method
    def transfer(self, amount, target_account):
        print(f"\n--- Initiating Transfer: ₹{amount} from {self.name} to {target_account.name} ---")
        if self.withdraw(amount):
            target_account.deposit(amount)
            print("Transfer Successful!")
        else:
            print("Transfer Cancelled.")

    def __str__(self):
        return f"{self.name}'s Account | Balance: ₹{self.balance}"


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)


# --- Testing ---
biswanath = Savings("Biswanath", 10000)
chandan = Current("Chandan", 5000)

print(biswanath)
print(chandan)

# Transfer 3000
biswanath.transfer(3000, chandan)

print("\n--- Final Balances ---")
print(biswanath)
print(chandan)

# Exceeding limit
chandan.transfer(10000, biswanath)