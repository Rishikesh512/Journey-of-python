class Courier:
    def deliver(self):
        print("Delivering by courier")

class Drone:
    def deliver(self):
        print("Delivering by drone")

class Pickup:
    def deliver(self):
        print("Customer pickup")

methods = [Courier(), Drone(), Pickup()]

for m in methods:
    m.deliver()
