def f(k, s, n):
    if k + s <= 53:
        return n == 2
    if n == 2:
        return False

    if n % 2 == 0:
        return any([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)])
    return any([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)])


for s in range(35, 1000):
    if f(19, s, 0):
        print(s)
        break