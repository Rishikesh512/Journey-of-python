a = {1,2,3,4}
b = {3,4,5,6}

common = a & b

a = a - common
b = b - common

print("Set A:", a)
print("Set B:", b)
