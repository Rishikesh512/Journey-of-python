from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts with key"

class Bike(Vehicle):
    def start(self):
        return "Bike starts with kick"

c = Car()
b = Bike()

print(c.start())
print(b.start())
