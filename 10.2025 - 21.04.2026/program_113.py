for x in range(1, 27001):
    y = 3*27**9+2*27**6+27**3-x
    k0= 0
    while y > 0:
        k0 += int(y%27==0)
        y //= 27
    if k0 == 6:
        print(x)
        break