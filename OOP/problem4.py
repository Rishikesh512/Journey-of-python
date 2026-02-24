class Car :

    def __init__(self,brand,model,colour,price):

        self.brand = brand
        self.model = model
        self.colour = colour
        self.price = price


    def details(self):

        print("Brand :-",self.brand)
        print("Model :-",self.model)
        print("Colour :-",self.colour)
        print("Price :-",self.price)

car1 = Car("Mahidra","Thar","Black",900000)

car2 = Car("Toyota","Fortuner","White",3500000)

car1.details()
car2.details()