
for x in range(3000, 0, -1):
    k = 0
    n = 9 * 11**210 + 8 * 11**150 - x
    while n > 0:
        if n % 11 == 0:
            k += 1
        n //= 11
    if k == 60:
         print(x)
         break
