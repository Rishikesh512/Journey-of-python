text = "ApplE OrAngE"
count = 0

for char in text:
    if char in "AEIOU":
        count += 1

print("Uppercase vowels:", count)
