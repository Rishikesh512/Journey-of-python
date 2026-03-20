from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
    
    def calculate_salary(self):
        return self.hours * self.rate

f = FullTimeEmployee(50000)
p = PartTimeEmployee(5, 500)

print("Full Time Salary:", f.calculate_salary())
print("Part Time Salary:", p.calculate_salary())
