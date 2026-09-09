with open('24_31230.txt') as f:
    s = f.readline()
    c = ''
    m = 1000000000000000000
    for i in range(len(s)):
        c += s[i]
        if c[-3:] == 'ABC':
            while c.count('ABC') > 110:
                if c[:+3] == 'ABC':
                    c = c[3:]
                else:
                    c = c[1:]
            c = c[c.find('ABC'):]

            if c.count('ABC') == 110 and c[-1] == 'C':
                m = min(m, len(c))
print(m)