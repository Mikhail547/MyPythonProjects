for x in range(1, 2031):
    s = 3**100 - x
    cnt0 = 0
    while s > 0:
        if s % 3 == 0:
            cnt0 += 1
        s //= 3
    if cnt0 == 5:
        print(x)