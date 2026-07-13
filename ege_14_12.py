cnt0 = 0
l = []
for x in range(1, 2031):
    s = 6**2030 + 6**100 - x
    while s > 0:
        if s % 6 == 0:
            cnt0 += 1
        s //= 6
    l.append(cnt0)
    cnt0 = 0
print(min(l))

