class Bus:
    def __init__(self, seats):
        self.seats = seats

    def reserve(self, n):
        if n <= self.seats:
            self.seats -= n
            print("Seats booked")
        else:
            print("Not enough seats")

b = Bus(20)
b.reserve(5)
b.reserve(18)
