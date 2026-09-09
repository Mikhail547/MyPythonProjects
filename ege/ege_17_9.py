x = [int(a) for a in open('17_31225.txt')]
y = []
m = max(a for a in x if a % 10 == 9 and len(str(a))== 4)
for i in range(len(x)-2):
    if sum(1 for a in x[i:i+3] if a % 10 == 9 and len(str(a))== 4) == 2 and sum(x[i:i+3]) < m:
        y.append(sum(x[i:i+3]))

print(len(y), max(y))
print(3/5)
