try:
    lst = [10, 20, 30, 40]
    index = int(input("Enter index: "))
    print("Element:", lst[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("Enter valid number")
