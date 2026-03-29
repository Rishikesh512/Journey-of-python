nums = [3, 5, 7, 9]

result = set()

for n in nums:
    for i in range(n):
        if i + (i+1) == n:
            result.add(n)

print("Sum of consecutive:", result)
