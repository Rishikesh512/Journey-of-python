class Parking:
    def __init__(self, slots):
        self.slots = slots

    def park_car(self):
        if self.slots == 0:
            print("Parking Full")
        else:
            self.slots -= 1
            print("Car parked")

    def exit_car(self):
        self.slots += 1
        print("Car exited")

    def available_slots(self):
        return self.slots


p = Parking(2)
p.park_car()
p.park_car()
p.park_car()
print("Available:", p.available_slots())
