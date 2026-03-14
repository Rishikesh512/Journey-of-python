class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Amit", 50000)
e1.show()
