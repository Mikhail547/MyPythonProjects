l = []
for _ in range(int(input())):
        l.append(input())
l.sort()
print(*l, sep='\n')