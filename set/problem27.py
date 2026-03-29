nums = [1, 2, 2, 3, 4, 4, 5]

result = set()

for i in range(1, len(nums)-1):
    if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
        result.add(nums[i])

print("Isolated elements:", result)
