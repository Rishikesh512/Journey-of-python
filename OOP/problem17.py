class Bank:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self):
        self.balance += self.balance * 0.05

b = Bank(1000)
b.add_interest()
print(b.balance)
