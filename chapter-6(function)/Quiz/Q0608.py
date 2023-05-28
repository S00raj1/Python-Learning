def check(*args):
    x = 0
    y = 0
    for i in args:

        if i % 2 == 0:
            x = i / 2 + x
        if i % 2 != 0:
            y = i * 2 + y

        y1 = x + y
    print(y1)


check(5, 6, 7, 8)
