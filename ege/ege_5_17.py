def f(a):
    s = bin(a)[2:]
    k = bin((sum(1 for n in s if n == '1')) % 2)[2:]
    k += k[-1]
    return int(s + k, 2)
for i in range(1, 1000):
    if f(i) > 60:
        print(i)
        break
