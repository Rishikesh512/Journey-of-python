def analyze_text(text):
    result = {
        "upper": 0,
        "lower": 0,
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "special": 0,
        "words": 0
    }

    freq = {}

    for char in text:
        # Frequency
        freq[char] = freq.get(char, 0) + 1

        # Upper / Lower
        if char.isupper():
            result["upper"] += 1
        elif char.islower():
            result["lower"] += 1

        # Digits
        elif char.isdigit():
            result["digits"] += 1

        # Special characters
        else:
            if char != " ":
                result["special"] += 1

        # Vowels / Consonants
        if char.isalpha():
            if char.lower() in "aeiou":
                result["vowels"] += 1
            else:
                result["consonants"] += 1

    # Word count
    result["words"] = len(text.split())

    # Most frequent character
    max_char = max(freq, key=freq.get)

    # Palindrome check
    clean_text = text.replace(" ", "").lower()
    is_palindrome = clean_text == clean_text[::-1]

    # Output
    print("\n--- Text Analysis ---")
    print("Uppercase:", result["upper"])
    print("Lowercase:", result["lower"])
    print("Vowels:", result["vowels"])
    print("Consonants:", result["consonants"])
    print("Digits:", result["digits"])
    print("Special Characters:", result["special"])
    print("Word Count:", result["words"])
    print("Most Frequent Character:", max_char)
    print("Palindrome:", is_palindrome)
    print("Character Frequency:", freq)


# Main program
text = input("Enter text: ")
analyze_text(text)