x = [int(a) for a in open('17_28762.txt')]
y = []
m = min(a for a in x if a % 23 ==0)
for i in range(len(x)-1):
    if x[i] % m == 0 or x[i+1] % m ==0:
        y.append(sum(x[i:i+2]))
print(len(y), max(y))
