def F(n):
    if n % 171 == 0:
        print(n, n//171, sep='\t')

for a in range(100):
    F(1230056 + a * 100)
for a in range(10):
    for b in range(100):
        F(10230056 + a *10**6 + b * 100)
