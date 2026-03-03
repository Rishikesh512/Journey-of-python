num = int(input("Enter any number :-"))
total = 0
for i in range(1,num):

    if num % i == 0:
        print(i)
        total += 1

print("All divisor of given number is :-",total)