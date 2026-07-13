n = int(input())
x = 0
c = 0
for i in range(n):
    x += 1
    for j in range(1, 9 + 1):
        c = x + j
        print(x, '+', j, '=', c)
    print()