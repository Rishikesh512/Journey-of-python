class Mobile:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def recharge(self, amount):
        self.balance += amount
        print("Recharged:", amount)

    def call(self, minutes):
        cost = minutes * 1   # ₹1 per minute
        if cost > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= cost
            print(f"Call of {minutes} minutes done")

    def check_balance(self):
        return self.balance


# Usage
m = Mobile("Rishikesh")

m.recharge(100)
m.call(30)
print("Balance:", m.check_balance())

m.call(80)   # test insufficient balance
print("Balance:", m.check_balance())
