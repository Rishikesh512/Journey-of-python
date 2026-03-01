class Input:
    def read(self):
        self.a = int(input("enter first number :-"))
        self.b = int(input("enter second number :-"))

class Operation:
    def add(self):
        self.sum = self.a + self.b

class Output(Input,Operation):
    def display(self):
        print("Sum :-",self.sum)

obj = Output()
obj.read()
obj.add()
obj.display()