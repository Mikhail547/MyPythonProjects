def M(x):
    for d in range(2, 1 + round(x**0.5)):
        if x % d == 0:
            return d + (x // d)
    return 0


y, k = 800000, 0
while k < 5:
    y += 1
    if M(y) % 10 == 4:
        k += 1
        print(y, M(y), sep="\t")


