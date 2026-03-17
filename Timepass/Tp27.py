class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    def display(self):
        print("Duck abilities:")

d = Duck()
d.display()
d.fly()
d.swim()
