s = 9**8 + 3**24 - 3 * 7
cnt2 = 0
x3 = ''
while s > 0:
    if s % 3 == 2:
        cnt2 += 1
    s //= 3
print(cnt2)
