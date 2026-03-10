num = 122334455
freq = {}

for digit in str(num):
    if digit in freq:
        freq[digit] += 1
    else:
        freq[digit] = 1

print(freq)
