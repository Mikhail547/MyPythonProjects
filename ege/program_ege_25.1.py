def F(a):
    m = a
    for d in range(2, 1 + round(a**0.5)):
        if a % d == 0 and d % 100 == 11 and d != 11:
            m = min(m, d)
        if a % d == 0 and (a//d) % 100 == 11 and (a//d) != 11:
            m = min(m, a//d)   
    return m
x, k = 1350050, 0
while k != 5:
    x+= 1
    if F(x)< x:
        k += 1
        print(x, F(x), sep='\t')
        
