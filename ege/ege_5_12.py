def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    return int(s, 2)
print(f(4), f(5))
N = 1
while f(N) < 190:
    N += 1
print(N)
