def f(k, t): # бинарный поиск
    cnt = t + k
    return cnt <= 240

n, k= map(int, input().split())
# n кол-во задач, k время до дома
left = 0
right = n # 3
ans = right
while left <= right:
    time = 0
    mid =(left + right) // 2 # 1 2
    for i in range(1, mid + 1):
        time += 5*i # 5 5 10
    if f(k, time):
        left = mid + 1 # 2
        ans = mid  # 1 2 3

    else:
        right = mid - 1
print(ans)








