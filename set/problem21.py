numbers = [1, 4, 6, 8, 3]
target = 10

seen = set()

for num in numbers:
    if target - num in seen:
        print("Pair found:", num, target - num)
        break
    seen.add(num)
