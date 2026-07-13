l = []
n = int(input())
for i in range(n):
    m = input()
    l.append(m)
k = int(input())
for i in range(len(l)):
    if len(l[i]) < k:
        continue
    print(l[i][k-1], end='')

