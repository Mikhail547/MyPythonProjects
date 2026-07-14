x = [int(a) for a in open('17_29349.txt')]
y = []
m = min(a for a in x if a > 0 and a % 123 == 0)
for i in range(len(x)-1):
    if x[i] + x[i+1] < m:
        y.append(x[i] + x[i+1])

print(len(y), abs(max(y)), sep='\t')



