numbers =[]

n = int(input("enter number :- "))

for i in range(n):
    num =float(input("enter number :-"))
    numbers.append(num)


total = sum(numbers)
average=total/n

print("Numbers:",numbers)
print("Total :-",total)
print("Average :-",average)
