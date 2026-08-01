s = open('24_26549.txt').readline()
c = ''
m = 0
for r in range(len(s)):
    c += s[r]
    if c[-4:] == '2025':
        while c.count('2025') > 50:
            c = c[1:]
        if c.count('2025') == 50 and c.count('Y') >= 140:
            m = max(m, len(c))
print(m)
