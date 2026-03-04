temperature = float(input("Enter temperature :-"))

if temperature < 0:
    print("Freezing")

elif temperature <= 15:
    print("Cold")

elif  temperature <= 30:
    print("Moderate")

else:
    print("Hot")
