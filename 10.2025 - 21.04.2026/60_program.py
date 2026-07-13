num = int(input())
n = 0
mid = num // 2 + 1
if n <= mid:
    for i in range(1, mid + 1):
        n += 1
        print(n * '*')
if n > mid - 1:
    for j in range(mid, 1, - 1):
        n -= 1
        print(n * '*')
