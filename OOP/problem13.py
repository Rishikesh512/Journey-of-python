class Bank:
    def bank_name(self):
        self.bank_name = input("Enter name of bank :-")

class Account:
    def account_type(self):
        self.account = input("Account type :-")

class Customer:
    def customer_name(self):
        self.name = input("enter customer name :-")

class Bank_Account(Bank,Account,Customer):
    def display(self):
        print("\n Account details :-")
        print("Bank Name :-",self.bank_name)
        print("Customer Name :-",self.name)
        print("Account Type :-",self.account)

obj=Bank_Account()

obj.account_type()
obj.customer_name()
obj.display()