def F(a):
    m = a
    for d in range(2, 1+round(a**0,5)):
        if a %d == 0 and d% 10 == 7 and d != 7:
            m = min(m, d)
        if a % d == 0 and (a // d) % 10 == 7 and (a // d) != 7:
            m = min(m, a // d)
        return m
x, k = 700_000, 0
while k < 5:
    x += 1
    if F(x) < x:
        print(x, F(x), sep='t')
        k += 1
