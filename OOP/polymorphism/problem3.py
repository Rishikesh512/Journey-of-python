class Shape:
    def draw(self):
        print("drawing shape")

class Circle(Shape):
    def draw(self):
        print("drawing circle")

class Rectangle(Shape):
    def draw(self):
        print("drawing a rectangle")

c = Circle()
r = Rectangle()

c.draw()
r.draw()