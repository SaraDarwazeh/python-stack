class User:

    def __init__(self, user_name="Sara", email="Tets@gmail.com"):
        self.name = user_name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount

    
    def make_withdrawal(self, amount):	
        if self.account_balance>amount:
            self.account_balance -= amount
        else:
            print("not enough balance")

    def display_user_balance(self):
        print("User:{},Balance{}".format(self.name,self.account_balance))

    def transfer_money(self, other_user, amount):
                if self.account_balance>amount:
                    self.make_withdrawal(amount)
                    other_user.make_deposit(amount)


                else:
                    print("not enough balance")
            

sara=User("sara","saradarwazeh14@gmail.com")
Ahmad=User("ahmad","aaa@gmail.com")
User3=User("Samer" , "Samer@gmail.com")

sara.make_deposit(3000)
sara.make_deposit(3000)
sara.make_deposit(3000)

sara.make_withdrawal(1000)
sara.display_user_balance()

Ahmad.make_deposit(10000)
Ahmad.make_deposit(2000)

Ahmad.make_withdrawal(1000)
Ahmad.display_user_balance()

User3.make_deposit(4000)
User3.make_withdrawal(1000)
User3.make_withdrawal(3000)
User3.make_withdrawal(1000)
User3.display_user_balance()


sara.transfer_money(User3,2000)
sara.display_user_balance()
User3.display_user_balance()