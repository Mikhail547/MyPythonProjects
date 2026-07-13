def f(a):
    cnt = a * 4
    return cnt <= n# - +


for i in range(int(input())):
    n = int(input()) # 4
    left = 0
    right = n // 4 # --max-- 2
    ans = 0
    while left <= right:
        mid = (left + right) // 2 # 1  0
        if f(mid):
            ans = mid
            left = mid + 1 # 1

        else:

            right = mid - 1 # 1
    leg = n - (ans * 4)
    ch = leg // 2

    print(ans + ch)
