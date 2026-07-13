def F(n):
    if n % 1917 == 0:
        print(n,n // 1917, sep='\t')
for a in range(10):
    for b in range(10):
        F(30120145+a*10**6+b*10**3)
for a in range(10):
    for b in range(10):
        for c in range(10):
            F(301201405+a*10**7+b*10**4+c*10)
for a in range(10):
    for b in range(10):
        for c in range(100):
            F(3012014005+a*10**8+b*10**5+c*10)

