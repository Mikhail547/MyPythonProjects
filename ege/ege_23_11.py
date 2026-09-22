x = [str(a) for a in open('23 text.txt')]
m = [[10001]*1001] * 1001
s = set()
for a in x:
    b,c,d = map(str, a.split())
    b, c = int(b), int(c)
    m[b][c] = d
    s.add(b)