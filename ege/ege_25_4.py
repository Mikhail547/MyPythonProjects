def F(n):
    if n % 271 == 0:
        print(n, n // 271, sep='\t')
for a in range(100):
    F(1200156 + a * 1000)
for a in range(100):
    for b in range(10):
        F(12001506 + a *10000 + b * 10)

