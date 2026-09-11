import sys
input = sys.stdin.readline

def two_points(n, k, arr):
    left = 0
    now_suma = ''
    m_length = 0
    ans = 0
    cnt_a = 0
    cnt_b = 0
    for right in range(len(arr)):
        now_suma += arr[right]
        if arr[right] == 'a':
            cnt_a += 1
        if arr[right] == 'b':
            cnt_b += 1
        while min(cnt_a,cnt_b ) > k:
            if arr[left] == 'a':
                cnt_a -= 1
            if arr[left] == 'b':
                cnt_b -= 1
            left += 1
        m_length = right - left + 1
        ans = max(m_length, ans)
    return ans

n, k = map(int, input().split())
arr = input().strip()
print(two_points(n, k, arr))
