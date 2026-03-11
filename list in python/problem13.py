nums = [23, 5, 78, 1, 34]

smallest = nums[0]

for i in nums:
    if i < smallest:
        smallest = i

print("Smallest:", smallest)
