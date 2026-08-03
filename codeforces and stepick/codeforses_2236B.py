def f(n, k, s):
    d = [0] * k
    for i in range(n):
        if s[i] == '1':
            d[i % k] += 1
    for i in range(len(d)):
        if d[i] % 2 != 0:
            return False
    return True


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if f(n, k, s):
        print('YES')
    else:
        print('NO')