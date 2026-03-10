data = {"a": 10, "b": 60, "c": 30, "d": 80}

result = {}

for key, value in data.items():
    if value <= 50:
        result[key] = value

print(result)
