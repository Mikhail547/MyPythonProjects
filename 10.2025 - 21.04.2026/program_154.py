n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
l.remove(max(l))
l.remove(min(l))


print(*l, sep='\n')


