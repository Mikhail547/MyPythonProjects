for x in range(0, 23):
    a = int('7610035', 23) + x*23**3
    b = int('3380932', 23) + x*23**3
    if (a + b) % 22 == 0:
        print((a + b) / 22)
        break
