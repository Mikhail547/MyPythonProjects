for x in range(100):
    for y in range(100):
        if (x + ((y - y **2)**0.5))*2**y*((x - x**2)**0.5) == 1:
            print(x, y)
