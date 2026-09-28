x = [str(a) for a in open('23_31518.txt')]
m = dict()
s = set()
for a in x:
    b,c,d = map(str, a.split())
    b, c = int(b), int(c)
    m[b*10000+c] = float(d)
    s.add(b)
    s.add(c)
for a in s:
    for b in s:
        if not(a*10000+b in m):
            m[a*10000+b] = 10**100
s.remove(1)
for k in range(1000):
    for b in s:
        for c in s:
            m[1 * 10000 + c] = min(m[1 * 10000 + b] + m[b * 10000 + c], m[1 * 10000 + c])
print(m[1*10000+100])
