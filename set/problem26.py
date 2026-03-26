nums = [2, 3, 8, 27]

s = set(nums)
result = {x for x in nums if x**3 in s}

print("Cube elements:", result)
