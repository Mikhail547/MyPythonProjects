def F(a, b):
    if b == 1:
        return 1
    if a == b:
        return 1
    if a < b:
        return 0
    total = 0
    for i in range(2, int((a**0.5)+1)):
        if a % i == 0:
            total +=  F(a //i, b)
            if i != a // i:
                total += F(i, b)
    return total
for i in range(int(input())):
    x, y = map(int, input().split())
    if F(x, y) > 0:
        print('YES')
    else:
        print('NO')
