def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

result = greatest(10, 25, 15)

print("Greatest number =", result)