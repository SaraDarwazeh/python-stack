class BankAccount:
    def __init__(self,interest,amount=0):
        self.amount=amount
        self.interest=interest
    
    def deposit(self, amount):
        self.amount += amount
        return self
    
    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.amount -= 5
        return self
    
    def yield_interest(self):
        self.amount += self.amount * self.interest
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.amount}")
        return self
    

saraaccount = BankAccount(interest=0.05, amount=100)
ahmedaccount= BankAccount(interest=0.02, amount=200)

saraaccount.deposit(50).deposit(100).deposit(25).withdraw(30).yield_interest().display_account_info()
ahmedaccount.deposit(75).deposit(25).withdraw(50).withdraw(100).withdraw(30).withdraw(20).yield_interest().display_account_info()


