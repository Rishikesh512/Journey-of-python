class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def fuel_type(self):
        print("Generic fuel type")


class electric_car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def fuel_type(self):
        print(f"{self.brand} runs on Electric Engine")

    def chargeBattery(self):
        print("Charging battery...")


class petrol_car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def fuel_type(self):
        print(f"{self.brand} runs on Petrol Engine")


class bicycle(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def fuel_type(self):
        print(f"{self.brand} does not need fuel")

    def pedalSpeed(self):
        print(f"Pedaling at {self.speed} km/h")


# सही object creation
e_car = electric_car("Tesla", 20)
p_car = petrol_car("Tata", 50)
b = bicycle("Hero", 10)

e_car.fuel_type()
p_car.fuel_type()
b.fuel_type()
b.pedalSpeed()