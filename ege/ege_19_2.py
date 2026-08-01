def f(a, b, n): # функция проверки числа и хода игрока
    if a+b >= 154 or n > 2:
        return n == 2
    if n % 2 == 0:
        return any([f(a +4, b, n+1),f(a *3, b, n+1), f(a, b +4, n+1), f(a, b *3, n+1) ])
    return any([f(a +4, b, n+1),f(a *3, b, n+1), f(a, b +4, n+1), f(a, b *3, n+1) ])
for s in range(1, 143):
    if f(11, s, 0):
        print(s)
        break