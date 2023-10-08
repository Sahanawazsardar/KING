# Check vowels in a string
vowels = ["a", "e", "i", "o", "u"]


def check_vowels():
    string = input("Please provide a string to check: ")
    v = ""
    for letter in string:
        for vowel in vowels:
            if vowel == letter:
                v += letter

    return len(v)


print(check_vowels())
