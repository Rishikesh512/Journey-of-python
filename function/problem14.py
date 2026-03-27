def count_types(s):
    upper = lower = digits = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
    return upper, lower, digits

print(count_types("PyThOn123"))
