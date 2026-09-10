import sys
input = sys.stdin.readline
def prefix_zero(arr):
    d = {0: 1}
    sum = 0
    for nowsum in arr:
        sum += nowsum
        if sum not in d:
            d[sum] = 0
        d[sum] += 1
    return d
def seach_higth(arr):
    ans = 0
    for nowsum in arr:
        ans += arr[nowsum] *(arr[nowsum]-1) //2
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = [int(a)-1 for a in input().strip()]
    k = prefix_zero(arr)
    print(seach_higth(k))

