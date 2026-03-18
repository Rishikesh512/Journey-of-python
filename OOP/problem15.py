class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = 0

    def mark_present(self):
        self.attendance += 1

    def show(self):
        print(self.name, self.attendance)

s = Student("Amit")
s.mark_present()
s.mark_present()
s.show()
