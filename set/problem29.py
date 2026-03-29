lists = [[1,2,3], [2,3,4], [3,4,5]]
k = 2

all_elements = set(sum(lists, []))
result = set()

for x in all_elements:
    count = sum(1 for lst in lists if x in lst)
    if count == k:
        result.add(x)

print("Exactly in k lists:", result)
