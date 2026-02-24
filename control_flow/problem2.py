#take year from user and check if it is a leap year
year = int(input("enter the year:"))

if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")

else:
    print("Not Leap Year")

