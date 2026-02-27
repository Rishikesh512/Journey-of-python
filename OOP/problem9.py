class Petrol_car:
    def Petrol_Engine(self):
        print("This car running on petrol engine")

class Electric_car:
    def Electric_Engine(self):
        print("This car running on electric engine")

class Hybridcar(Petrol_car,Electric_car):
    def start(self):
        print("Hybrid car starting....")
        self.Petrol_Engine()
        self.Electric_Engine()

car = Hybridcar()
car.start()
