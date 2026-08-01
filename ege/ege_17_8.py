x = [int(a) for a in open('17_31155.txt')]
y = []
k = len([a for a in x if abs(a) % 100 == 0])
for i in range(len(x)-1):
    if min(x[i:i+2]) < 0 and sum(x[i:i+2]) <k:
        y.append(sum(x[i:i+2]))
print(len(y), max(y), sep='\t')
