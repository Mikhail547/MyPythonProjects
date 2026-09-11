import sys
input = sys.stdin.readline

def f(n, s):
    m = 0
    a = [0] * (n+1)
    p = [0] *(n+1)
    if all('0'in a for a in s) or s[0] == '0' :
        return -1
    for i in range(1, n+1):
        if s[i-1] == '+':
            if p[i-1] <= 0:
                a[i] = -(p[i-1]) + 1
                p[i] = p[i-1] + a[i]
            if p[i-1] > 0:
                if p[i-1] - 1 > 0:
                    a[i] = -1
                    p[i] = p[i - 1] + a[i]
        if s[i-1] == '-':
            if p[i-1] >= 0:
                a[i] = -(p[i-1]) - 1
                p[i] = p[i-1] + a[i]
            if p[i-1] < 0:
                if p[i-1] + 1 < 0:
                    a[i] = 1
                    p[i] = p[i - 1] + a[i]
        if s[i-1] == '0':
            a[i] = -p[i-1]
            p[i] = p[i-1] + a[i]

    return min(abs(x) for x in a if x != 0)

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(f(n, s))
    # всё неправильно, нужно переделать с указателями