class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(4), Circle(3)]

for s in shapes:
    print(s.area)
