x = [int(a) for a in open('17_29971.txt')]
y = []
m = max(a for a in x if a % 100 == 33)
for i in range(len(x)-2):
        if sum(1 for a in x[i:i+3] if 10 <= abs(a) < 100) == 2 and sum(x[i:i+3])**2 < m:
            y.append(sum(x[i:i+3]))
print(len(y), max(y))
