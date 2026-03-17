class Buyer:
    def buy(self):
        print("Buying product")

class Seller:
    def sell(self):
        print("Selling product")

class User(Buyer, Seller):
    pass

u = User()
u.buy()
u.sell()
