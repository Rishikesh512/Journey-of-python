def add(a,b):
    return a + b
def substract(a,b):
    return a - b 
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0 :
        return "cannot devide by zero"
    return a / b
  
print("Simple calculator")
print("1.Add")
print("2.substract")
print("3.Multiply")
print("4.Divide")

operation =int(input("enterr the operation(1-4):"))

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))

if operation == 1:
    print("Result:",add(num1,num2))

elif operation == 2:
    print("Result:",substract(num1,num2))

elif operation == 3:
     print("Result:",multiply(num1,num2))

elif operation == 4:
     print("Result:",divide(num1,num2))
    
else:
    print("Invalid choice")


    
