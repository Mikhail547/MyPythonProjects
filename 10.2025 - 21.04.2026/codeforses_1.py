def f(mid, w, h, n):
    count = (mid // w) * (mid//h)
    return count >= n
w, h, n = map(int, input().split())

left = 0
right = max(h, w) * n
ans = right

while left <= right:
    mid = (left + right) // 2
    if f(mid, w, h, n):
        ans = mid
        right = mid -1
    else:
        left = mid + 1
print(ans)





