lists = [[1,2,3], [2,3,4], [3,4,5]]

freq = {}

for lst in lists:
    for x in set(lst):
        freq[x] = freq.get(x, 0) + 1

group = {}

for x, count in freq.items():
    group.setdefault(count, []).append(x)

print("Grouped by frequency:", group)