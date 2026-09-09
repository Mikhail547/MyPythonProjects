import sys
input = sys.stdin.readline

def prefix(arr):
    h = [0] * (len(arr)+1)
    for i in range(1, len(arr)+1):
        h[i] = h[i-1] + arr[i-1]
    return h
n = int(input())
arr = [int(a) for a in input().split()]
pref1 = prefix(arr)
pref2 = prefix(sorted(arr))
m = int(input())
for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(pref1[r] - pref1[l-1])
    else:
        print(pref2[r] - pref2[l-1])





