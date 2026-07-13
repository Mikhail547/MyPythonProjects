with open('24_25361.txt') as f:
    s = f.readline()
    for a in '2468':
        s = s.replace(a,'0')
    s = s.split('0')[1:]
    m = 76
    for a in s:
        if  a.count('F') >= 76:
            b = a.split('F')[:77]
            s = sum(len(c) for c in b) + 77
            m = max(m, s)
print(m)