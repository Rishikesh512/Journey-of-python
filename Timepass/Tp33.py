class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def makesound(self):
        print("Animal make sound")

class Dog(Animal):
    def makesound(self):
        print("Dog is barking")

 

class Cat(Animal):
    def makesound(self):

        print("cat is mewing")


class Bird(Animal):
    def makesound(self):

        print("quake quake")

    def move(self):
        print("Flying")


dog =Dog("Moti",5)
cat = Cat("Mani",4)
bird = Bird("Parrot",2)

dog.makesound()
cat.makesound()
bird.makesound()
bird.move()


        
       

        