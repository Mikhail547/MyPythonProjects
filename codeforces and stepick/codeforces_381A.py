import sys
input = sys.stdin.readline
def two_points(n, arr):
    right = n-1
    left = 0
    s_sum = 0
    p_sum = 0
    for i in range(0, n):
        if i % 2 == 0:
            s_sum += max(arr[right], arr[left])
            if arr[right] > arr[left]:
                right -= 1
            else:
                left += 1
        else:
            p_sum += max(arr[right], arr[left])
            if arr[right] > arr[left]:
                right -= 1
            else:
                left += 1
    ans = []
    ans.append(s_sum)
    ans.append(p_sum)
    return ans

n = int(input())
arr = list(map(int, input().split()))
print(*two_points(n, arr))


