def f(a, n): # a - кол-во камней. n - номер хода игрока
    if a >= 29 or n > 2:
        return n == 2
    if n % 2 == 0:
        return all([f(a + 1, n +1), f(a * 2, n +1)])
    return any([f(a+1, n+1), f(a*2, n+1)])

for s in range(1, 28):
    if f(s, 0):
        print(s)

