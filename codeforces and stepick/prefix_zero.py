import sys
input = sys.stdin.readline

def dict1(arr):
    prefix_zero = {0:1}
    nowsum = 0
    for now in arr:
        nowsum += now
        if nowsum not in prefix_zero: #  проверяем каждую сумму, если не встречалас, то =1 иначе x+1
            prefix_zero[nowsum] = 0
        prefix_zero[nowsum] += 1
    return prefix_zero

def seach_hight(prefix_zero):
    ans = 0
    for nowsum in prefix_zero:
        cntsum = prefix_zero[nowsum]
        ans += cntsum * (cntsum-1) // 2 # формула сочетаний на отрезках
    return ans
arr = [int(a) for a in input().split()]
d = dict1(arr)
print(seach_hight(d))

