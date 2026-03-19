class Multiply:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

m = Multiply(3)
print(m(5))   # acts like function
