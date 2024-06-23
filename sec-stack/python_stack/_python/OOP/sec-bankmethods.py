class User:

    def __init__(self, user_name="Sara", email="Tets@gmail.com"):
        self.name = user_name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    
    def make_withdrawal(self, amount):	
        if self.account_balance>amount:
            self.account_balance -= amount
        else:
            print("not enough balance")
        return self

    def display_user_balance(self):
        print("User:{},Balance{}".format(self.name,self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
                if self.account_balance>amount:
                    self.make_withdrawal(amount)
                    other_user.make_deposit(amount)
                else:
                    print("not enough balance")
                return self


sara=User("sara","saradarwazeh14@gmail.com")


sara.make_deposit(3000).make_deposit(3000).make_deposit(3000).make_withdrawal(1000).display_user_balance()

