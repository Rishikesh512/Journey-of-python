class Vehicle :
    def __init__(self,brand,speed):
        self.brand =  brand
        self.speed = speed


    def fuel_type(self):
        print("Fuel type")


class electric_car(Vehicle):

    def __init__(self,brand,speed):
        print("This car runs on electric Engine")
        super().__init__(self)
    

class petrol_car(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(self,brand,speed)
        print("this car run on petrol engine ")

class bicycle(Vehicle):

    print("pedal")


e_car= ("tesla",20)
p_car = ("Tata",50)
b = ("Hero",10)

e_car.fuel_type()
p_car.fuel_type()
b.fuel_type()