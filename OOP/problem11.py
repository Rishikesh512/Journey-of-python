class person:
    def get_person(self):
        self.name = input("Enter name :-")
        self.age = input("Enter age")

class employee :
    def get_employee(self):
        self.emp_id = input("Enter id :-")

class Manager(person,employee) :
    def display(self):
        print("Name :-",self.name)
        print("Age :-",self.age)
        print("Employee ID :-",self.emp_id)

m = Manager()
m.get_person()
m.get_employee()
m.display()