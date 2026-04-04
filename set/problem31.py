lists = [[1,2,3], [2,3,4], [3,4,5]]

all_elements = set(sum(lists, []))
result = set()

for x in all_elements:
    if any(x not in lst for lst in lists):
        result.add(x)

print("Missing in at least one list:", result)
