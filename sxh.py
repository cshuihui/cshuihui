def sxh():
    for i in range(100, 1000):
        a = (int)(i / 100)
        b = (int)((i - a * 100) / 10)
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i, end=' ')

sxh()

