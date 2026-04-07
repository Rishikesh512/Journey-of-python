strs = input("Enter words separated by space: ").split()

prefix = strs[0]

for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)
