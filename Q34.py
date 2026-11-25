def count_characters(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1

    return upper, lower

text = input("Enter a string: ")

u, l = count_characters(text)

print("Uppercase characters =", u)
print("Lowercase characters =", l)