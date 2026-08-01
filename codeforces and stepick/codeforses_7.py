def f(m, k, n, N):
    k_1 = k
    l = 0
    for i in range(n-1):

        if k >= m:
            return l
        if k < N[i]:
            return -1

        if k > N[i] and k >= N[i+1]:
            continue
        if k >= N[i] and k < N[i+1]:
            k = k_1 + int(N[i])
            l += 1
    if k >= m:
        return l
    if k < N[i]:
        return -1
    if k >= N[n-1] and k < m:
        k = k_1 + int(N[i])
        l += 1
    if k >= m:
        return l
    if k < m:
        return -1


m, k, n = map(int, input().split())
# m - путь, k - бак, n - кол-во заправок
N = [int(a) for a in input().split()]

print(f(m, k, n, N))

