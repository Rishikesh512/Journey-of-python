str = input("enter any sentence").lower()

upper =  0
lower = 0

for ch in str :
    if ch.isupper():
     upper  += 1
    elif ch.islower():
      lower += 1

print("Uppercase letters:",upper)
print("Lowercase letters",lower)