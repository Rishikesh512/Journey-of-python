class Person:
    def __init__(self):
        self.__age = 0

    
    def age(self):
        return self.__age

   
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age")


p = Person()
p.age = 25
print("Age:", p.age)
