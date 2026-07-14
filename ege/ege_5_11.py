def f(n):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
        l = [a for a in s]
        l[1] = '0'
        s = ''.join(l)
        return int(s, 2)
    else:
        s += '1'
        l = [a for a in s]
        l[1] = '1'
        s = ''.join(l)
        return int(s, 2)
m = []
print(f(6), f(4))
for i in range(1, 1+1000):
    if f(i) < 19:
        m.append(i)
print(max(m))


