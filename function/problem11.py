class Bank_Account:
    def __init__(self,name,balance):
        self.name = name 
        self.balance = balance

    def display(self):
        print("Account Holder :-",self.name)

        print("Balance:-",self.balance)

name =input("Enter account holder name :")

balance =float(input("Enter your balance :"))


acc1 =Bank_Account(name,balance)

acc1.display()