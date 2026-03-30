class Payment:
    def pay(self, amount):
        print("Processing payment")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card 💳")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI 📱")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash 💵")


# Usage
payments = [CreditCard(), UPI(), Cash()]

for p in payments:
    p.pay(1000)