class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :-",self.brand)
        print("Model :-",self.model)

c1 = car("Toyota","Fortuner")

c1.display()
