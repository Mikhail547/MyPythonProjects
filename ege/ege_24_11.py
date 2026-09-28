s = open('24_17878.txt').readline()
z2 = ['--', '**', '*-', '-*']
z3 = ['-00', '*00', '-06', '*06', '-07', '*07', '-08', '*08', '-09', '*09']
z4 = ['00', '06', '07', '08', '09']
t, m = '', ''

for a in s:
    t += a
    if t[0] in '-*':
        t = t[1:]
    if len(t) > 1 and t[-2:] in z2:
        t = ''
    if len(t) > 1 and t[:2] in z4:
        t = t[1:]
    if len(t) > 2 and t[-3:] in z3:
        t = t[-1]
    if len(t) > len(m) and not (t[-1]  in '-*'):
        m = t
        print(len(m), m)