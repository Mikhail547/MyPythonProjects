x = [int(a) for a in open('17_31335.txt')]
y = []
m = min(a for a in x if a >0 and a % 9 == 0)
for i in range(len(x)-1):
    if x[i] != x[i+1] and abs(x[i] - x[i+1]) % m == 0:
        y.append(sum(x[i:i+2]))
print(len(y), max(y))

