class Transport:
    def travel(self):
        pass

class Bus(Transport):
    def travel(self):
        print("Travel by Bus")

class Train(Transport):
    def travel(self):
        print("Travel by Train")

class Flight(Transport):
    def travel(self):
        print("Travel by Flight")

t = [Bus(), Train(), Flight()]

for i in t:
    i.travel()
