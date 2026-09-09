x = [int(a) for a in open('17_31514.txt')]
y = []
m = min(x)
for i in range(len(x)-1):
    if x[i]%33 == m or x[i+1]%33 == m:
        y.append(sum(x[i:i+2]))
print(len(y), max(y), sep='\t')
