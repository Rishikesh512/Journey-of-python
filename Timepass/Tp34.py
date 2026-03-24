class Employee:
    def __init__(self,name,id,base_salary):

        self.name = name
        self.id = id
        self.base_salary = base_salary
    
    def calculatepay(self):
        print("_")

class FullTimeEmployee(Employee):
    def calculatepay(self):
        return self.base_salary 


class PartTimeEmployee(Employee):
    def __init__(self,name,emp_id,base_salary,fixed_salary,hourley_rate,contract_rate):

        self.fixed_salary = fixed_salary
        self.hourley_rate = hourley_rate
        self.contract_rate = contract_rate
        super().__init__(name,emp_id,base_salary)
       
       

    def calculatepay(self):
        return self.hourley_rate * self.base_salary

class Contractor(Employee):
    def __init__(self, name, emp_id, contract_rate, projects_completed):
      
        self.contract_rate = contract_rate
        self.projects_completed = projects_completed
        super().__init__(name,emp_id)
    def calculatepay(self):
        return self.contract * self.project_completed
    

emp1=FullTimeEmployee("Rutik",5737,20000)

emp2= PartTimeEmployee("Ram",4317,40000,20000,10000,45)

emp3 = Contractor("Sumit",9098,60000,54)


print(f"{emp1.name} Salary:{emp1.calculatepay()}")

print(f"{emp2.name} Salary:{emp2.calculatepay()}")


print(f"{emp3.name} Salary:{emp3.calculatepay()}")

