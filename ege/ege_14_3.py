for x in range(3000, 0, -1):
    y = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    k0 = 0
    while y> 0:
        k0 += int(y % 11 == 0)
        y //= 11
    if k0 == 60:
        print(x)
        break
    