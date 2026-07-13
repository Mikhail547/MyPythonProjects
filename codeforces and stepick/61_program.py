for n in range(1, 366):
    for k in range(1, 366):
        for m in range(1, 366):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
                