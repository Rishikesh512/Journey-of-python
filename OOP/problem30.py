class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


p = Product(500)
print("Price:", p.get_price())

# p.__price = 1000  # This won't change actual private value
print("Price after attempt:", p.get_price())
