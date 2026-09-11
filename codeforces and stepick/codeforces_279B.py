import sys
input = sys.stdin.readline

def two_poincst(n, t, arr): # метод двух указателей по бегущей строке, ищу max строку 1 <= m < t
    left = 0
    m_length = 0
    sum_a = 0
    for right in range(n):
        sum_a += arr[right]
        while sum_a > t:
            sum_a -= arr[left]
            left += 1
        current_length = right - left + 1
        m_length = max(m_length, current_length)
    return m_length
n, t = map(int, input().split())
arr = [int(a) for a in input().split()]
print(two_poincst(n, t, arr))




