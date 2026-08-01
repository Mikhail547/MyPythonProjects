def f(a, b, n):
    if a+b >= 154 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(a +4, b, n+1),f(a *3, b, n+1), f(a, b +4, n+1), f(a, b *3, n+1) ])
    return any([f(a +4, b, n+1),f(a *3, b, n+1), f(a, b +4, n+1), f(a, b *3, n+1) ])
for s in range(1, 143):
    if f(11, s, 0):
        print(s)
        