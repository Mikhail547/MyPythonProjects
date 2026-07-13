for n in range(1, 10000):
    for m in range(1, 10000):
        if (n * m) - ((3 * n + 7 * m) * 2) == 5:
            print(m)