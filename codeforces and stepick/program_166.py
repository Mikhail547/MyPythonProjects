n = input()
n = int(n[1:])
l = []
for i in range(n):
    l.append(input())
for i in range(n):
    s = str(l[i])
    if '#' in l[i]:
        x = s.find('#')
        s = s[:x]
        s = s.rstrip()
    s = s.rstrip()
    l[i] = s

for i in l:
    print(i)


