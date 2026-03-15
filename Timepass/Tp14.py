#sum of evwn number 1 to 20
n = int(input("enter the n :"))
sum = 0
for i in range (1,n+1):


    if i % 2 == 0 :

        sum += i

print("Sum of all even number is :-",sum)