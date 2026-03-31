class Vehicle :
    def __init__(self,brand,speed):
        self.brand =  brand
        self.speed = speed


    def fuel_type(self):
        print("Fuel type")


class electric_car(Vehicle):

    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        print("This car runs on electric Engine")
    

class petrol_car(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        print("this car run on petrol engine ")

class bicycle(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        print("pedal")


e_car= electric_car("tesla",20)
p_car = petrol_car("Tata",50)
b = bicycle("Hero",10)

e_car.fuel_type()
p_car.fuel_type()
b.fuel_type()