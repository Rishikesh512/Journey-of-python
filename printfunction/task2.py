y =int(input("Enter the y:"))

if y%400==0 :
    print("this is leap year")

elif y%100==0 :
    print("this is not leap year")
elif y%4==0  :
    print("this is leap year")
else:
    print("not leap year")