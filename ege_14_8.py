for x in range(1, 2031):
    cnt0 = 0
    s = 7**91 + 7**160 - x
    while s > 0:
        if s % 7 == 0:
            cnt0 += 1
        s //= 7
    if cnt0 == 70:
        print(x)
