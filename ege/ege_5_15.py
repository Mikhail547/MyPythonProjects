def f(a):
    s = bin(a)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
        s = '10' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]
    return int(s, 2)

m = min(a for a in range(1, 100) if f(a) >= 16)
print(m)