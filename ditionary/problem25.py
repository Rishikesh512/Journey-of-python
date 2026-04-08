text = "apple banana orange umbrella cat"
words = text.split()

count = 0
for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Words starting with vowel:", count)
