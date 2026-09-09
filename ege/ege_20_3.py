def f(k, s, n):
    if s + k <= 53:
        return n == 3
    if n == 3:
        return False
    if not(n % 2 == 0):
        return all([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)])
    return any([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)])

for s in range(1000, 34, -1):
    if f(19, s, 0):
        print(s)
        break