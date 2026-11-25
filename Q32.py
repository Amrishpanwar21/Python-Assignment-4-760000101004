def add(*args):
    total = 0

    for num in args:
        total = total + num

    print("Sum =", total)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)