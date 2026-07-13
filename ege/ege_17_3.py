x = [int(n) for n in open('ege_17_3.txt') ]
y = []
m = max(n for n in x if 999 < abs(n) < 10000 and n % 100 == 43)
for i in range(len(x)-1):
    k = len([a for a in x[i:i+2] if 999< abs(a) < 10000])
    if k > 0 and sum(x[i:i+2])**2 < m**2:
        y.append(sum(x[i:i+2])**2)
print(len(y), max(y))