def count_vowels():
    text = input("Enter a string: ")

    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    print("Total vowels =", count)

count_vowels()