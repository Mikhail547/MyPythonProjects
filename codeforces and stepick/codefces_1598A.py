import sys
input = sys.stdin.readline

def f(n, k):
    for i in range(0, n+1):
        if k[(1, i)] == '1' and k[(2, i)] == '1':
            return False
    return True


for i in range(1, int(input())+1):
    n = int(input())
    k = {}
    s1 = input()
    s2 = input()
    for j in range(0, n+1):
        k[(1, j)] = s1[j]
        k[(2, j)] = s2[j]
    if f(n, k):
        print('YES')
    else:
        print('NO')
