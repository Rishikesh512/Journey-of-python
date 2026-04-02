class Wallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount

    def spend(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print("Spent:", amount)

    def show_balance(self):
        return self.balance


w = Wallet()
w.add_money(1000)
w.spend(400)
print("Balance:", w.show_balance())
