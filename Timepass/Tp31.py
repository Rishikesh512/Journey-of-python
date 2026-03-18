class Hotel:
    def __init__(self, total):
        self.total = total
        self.booked = 0

    def book(self):
        if self.booked < self.total:
            self.booked += 1

    def cancel(self):
        if self.booked > 0:
            self.booked -= 1

    def available(self):
        return self.total - self.booked

h = Hotel(10)
h.book()
h.book()
h.cancel()
print(h.available())
