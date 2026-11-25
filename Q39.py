a = 10

def change():
    global a
    a = 50

change()

print("Updated value =", a)