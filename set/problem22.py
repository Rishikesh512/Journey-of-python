nums = [1, 5, 3, 4, 2]
k = 2

s = set(nums)

for num in s:
    if num + k in s:
        print((num, num + k))
