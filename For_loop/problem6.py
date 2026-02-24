#Count digit in number

num = int(input("Enter the number:"))
count = 0 

for digit in str(num) :
    count +=1

    print("Total digit:",count)