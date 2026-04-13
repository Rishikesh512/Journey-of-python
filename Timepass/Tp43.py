s = input("Enter string: ")
count = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            count += 1

print("Total palindromic substrings:", count)