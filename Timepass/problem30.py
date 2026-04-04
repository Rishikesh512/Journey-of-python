lists = [[1,2,3], [2,3,4], [3,4,5]]

result = set(lists[0])

for lst in lists[1:]:
    result = result & set(lst)

print("Common in all lists:", result)
