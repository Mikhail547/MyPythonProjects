from itertools import count

n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
print(*l, sep='\n')




