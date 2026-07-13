with open('24_28943.txt') as f:
    s = f.readline()
    for i in 'AEIOUY':
        s = s.replace(i, 'A')
l = s.split('A')
cnt = []

for i in range(len(l) -1):
    d = l[i] + 'A'
    if d.count('20') >= 26:
        ind = d.split('20')

        d_m = ind[-27:]

        m = '20'.join(d_m)


        cnt.append(len(m))

print(min(cnt))
