n = int(input())
cnt = 0
while n > 0:
    if n - 5 >= 0:
        n -= 5
        cnt += 1
    elif n - 4 >= 0:
        n -= 4
        cnt += 1
    elif n - 3 >= 0:
        n -= 3
        cnt += 1
    elif n -2 >= 0:
        n -= 2
        cnt += 1
    elif n - 1 >= 0:
        n -= 1
        cnt += 1

print(cnt)
