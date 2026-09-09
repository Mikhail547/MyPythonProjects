for x in range(22):
    a = int('27098876', 22) + x*22**5
    b = int('26051', 22) + x * 22 ** 2
    c = int('71105', 22) + x*22
    if (a+b+c) % 21 == 0:
        print(x, (a+b+c)//21)