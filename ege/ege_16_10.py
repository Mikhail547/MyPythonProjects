for x in range(2030, 0, -1):
    y = 7**170 + 7**100 - x
    k0 = 0
    while y >0:
        k0 += int(y % 7 == 0)
        y //= 7
    if k0 == 71:
        print(x)
        break
