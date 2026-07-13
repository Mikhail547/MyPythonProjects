l = []
s = int(input())
ln = int(input())
for i in range(s-1):
    n = int(input())
    l.append(ln+n)
    ln = n
print(l)
