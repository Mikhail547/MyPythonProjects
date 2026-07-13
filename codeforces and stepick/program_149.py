l = []
n = int(input())
m = 0
for i in range(n):
    m = int(input())
    l.append(m)
del l[1::2]
print(l)
