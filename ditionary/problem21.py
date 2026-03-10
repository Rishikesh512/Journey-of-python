text = "PyThOn"
count = {"upper": 0, "lower": 0}

for char in text:
    if char.isupper():
        count["upper"] += 1
    elif char.islower():
        count["lower"] += 1

print(count)
