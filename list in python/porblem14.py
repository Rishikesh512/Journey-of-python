nums = [-3, 5, -1, 7, -8, 2]

pos = 0
neg = 0

for i in nums:
    if i > 0:
        pos += 1
    else:
        neg += 1

print("Positive:", pos)
print("Negative:", neg)
