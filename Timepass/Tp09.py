class Student:
    def set_student(self):
        self.name = "Rahul" 
        self.roll_no = 34

class Mark:
    def set_marks(self):
        self.marks = 98

class Result(Student,Mark):
    def display(self):
        print("Name :-",self.name)
        print("Roll no. :-",self.roll_no)
        print("Marks :-",self.marks)


r = Result()
r.set_student()
r.set_marks()
r.display()