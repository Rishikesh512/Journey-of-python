def frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(frequency([1, 2, 2, 3, 3, 3]))
