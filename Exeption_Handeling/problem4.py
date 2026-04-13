correct_password = "1234"

attempts = 0

while attempts < 3:
    try:
        password = input("Enter password: ")

        if password != correct_password:
            attempts += 1
            print("Wrong password")

        else:
            print("Login successful")
            break

    except Exception:
        print("Error occurred")

if attempts == 3:
    print("Account locked")
