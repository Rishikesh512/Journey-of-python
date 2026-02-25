numbers = []
even = []
odd = []

n =int(input("How many number? "))

for i in range(n):
    num = int(input("Enter number :"))
    numbers.append(num)

for num in numbers :
    if num%2==0:
        even.append(num)
    
    else:
        odd.append(num)

print("even numbers:-",even)
print("odd numbers;-",odd)