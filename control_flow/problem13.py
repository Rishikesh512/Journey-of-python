password =input("Enter the password :-")

if len(password) < 6 :
    print("Weak password")

elif len(password) <= 10:
    print("Medium password")

elif len(password) > 10 and any (char.isdigit() for char in password):
    print("Strong password")

else:
    print("Medium password")