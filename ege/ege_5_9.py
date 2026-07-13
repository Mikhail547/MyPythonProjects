def R(N):
    k = ''
    while N >0:
        k += str(N % 3)
        N //= 3
    k = k[::-1]

    if N % 3 == 0:
        k += k[-2:]
    else:
        n = 0
        d = int(k)
        while d > 0:
            n += d % 10
            d //= 10
        n *= 2
        n3 = ''
        while n > 0:
            n3 += str(n %3)
            n //= 3
        n3 = n3[::-1]

        k += n3
        print(k)

    return int(k, 3)
print(R(8), R(9))
m = min(R(a) for a in range(1, 10000) if R(a) > 520 and R(a) %2 != 0)
print(m)
