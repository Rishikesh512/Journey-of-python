numbers = [1, 2, 3, 4, 5]
result = {}

for num in numbers:
    if num % 2 == 0:
        result[num] = "Even"
    else:
        result[num] = "Odd"

print(result)
