def count_substring(s, sub):
    return s.count(sub)

print(count_substring("banana", "an"))
def find_pairs(lst, target):
    pairs = []
    seen = set()
    
    for num in lst:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
        
    return pairs

print(find_pairs([1, 2, 3, 4, 5], 6))
