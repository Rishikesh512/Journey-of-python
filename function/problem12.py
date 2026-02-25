class User :
    def __init__(self,username,email):
        self.username = username
        if "@" in email:
            self.email = email
        else:
            self.email = "Invalid Email"

    def display(self):
        print("Username:",self.username)
        print("Email :",self.email)


u1 = User("rahul 123","rahul@gamil.com")
u2 = User("john453","johnmail.com")

u1.display()
u2.display()

        