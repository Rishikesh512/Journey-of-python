class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
            print(self.name,"says bhav bhav!")

    def details(self):
            print("Dog name :",self.name)
            print("Dog age",self.age)


dog1 = Dog("Tommy",6)

dog2 = Dog("Moti",8)


dog1.details()
dog1.bark()
dog2.details()
dog1.bark()