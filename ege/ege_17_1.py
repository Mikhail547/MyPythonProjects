with open ('DEMO_17.txt') as f:
    x = [int(a) for a in f]
    y = []
    m = min(a for a in x if 10 <= a <= 99)
    for i in range(len(x) - 1):
        k = len([a for a in x [i:i +2] if 10 <= a <= 99 ])
        if k == 1 and sum (x [i:i +2]) % m == 0:
            y.append (sum (x[i:i +2]))
print(len(y), max(y), sep='\t')