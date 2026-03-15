num = input("enter the num :-")

even = 0
odd = 0 

for digit in num:
    if int(digit)%2 == 0:
        even += 1

    else:
        odd += 1

print("Even digits :-",even)
print("odd digits :-",odd)