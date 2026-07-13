m = 0
m_x = []
m_d = []

for x in range(1, 2030):
    d = 5**150 + 5**100 - x
    k_d= ''
    k_x = ''
    while d >0:
        k_d += str(d%5)
        d //= 5
    while x >0:
        k_x += str(x%5)
        x //= 5
    k_d = k_d[::-1]
    k_x = k_x[::-1]
    if k_d.count('0') > m:
        m = k_d.count('0')
        m_d.append(k_d.count('0'))
        m_x.append(k_x)
m_x = [int(a, 5) for a in m_x]

print(m_d)
print(m_x)
print(int('4', 5))


