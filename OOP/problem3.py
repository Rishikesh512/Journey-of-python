class Student :

    def __init__(self,name,standerd,roll_no,branch):

        self.name = name
        self.standerd = standerd
        self.roll_no = roll_no
        self.branch = branch

    def display(self):
        print("Name :-",self.name)
        print("ROLL NO. :-",self.roll_no)
        print("Standerd :-",self.standerd)
        print("Branch :-",self.branch)

s1 = Student("rushikesh",12,46,"Art")

s2 =Student("Rutik",11,45,"Art")

s1.display()
s2.display()