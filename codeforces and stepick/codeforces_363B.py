import sys
input = sys.stdin.readline

def prefixsum(arr): # здесь алгоритм префиксных сумм
    pref = [0] * (len(arr) + 1)
    for i in range(1, len(arr)+1):
        pref[i] = pref[i-1] + arr[i-1]
    return pref
n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = prefixsum(arr)
m = l[k] - l[0]
f = 1
for i in range(1, n-k+1): # поиск наименьшей суммы на полуотрезке k-1
    if l[i + k] - l[i] < m:
        m = l[i + k] - l[i]
        f = i + 1
print(f)




