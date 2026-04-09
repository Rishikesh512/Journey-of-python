text = "programming"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

count = 0
for v in freq.values():
    if v == 1:
        count += 1

print("Unique occurring chars:", count)
