class Animal :
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is :-{self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Hello your name is :-{self.name},{self.age}")

  
animal1 = Animal("Lion")
person1 =Human("Rushikesh",21)

person1.show()
animal1.show()