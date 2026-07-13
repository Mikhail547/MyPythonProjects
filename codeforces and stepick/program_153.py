n = int(input())
x = []
y = []
for i in range(n):
    num = int(input())
    x.append(num)
for i in  range(n):
    num = (x[i] + 1)**2
    y.append(num)
print(*x, sep='\n')
print()
print(*y, sep='\n')

