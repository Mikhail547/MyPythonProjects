def f(a):
    s = bin(a)[2:]
    if a % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    return int(s, 2)

m = f(17)
for i in range(18, 1000):
    if f(i) < m:
        m = f(i)
print(m)


print(144000*24*138 / 8 / 1024 / 1024) # 476928000 bit
