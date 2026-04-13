balance = 5000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        raise Exception("Insufficient balance")

    balance -= amount
    print("Remaining balance:", balance)

except ValueError:
    print("Enter valid amount")

except Exception as e:
    print(e)
