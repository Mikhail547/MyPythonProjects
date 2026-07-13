a = int(input())
b = int(input())
n = 0
for i in range(a, b + 1):
        if i == 1:
                continue
        if (i % 2 != 0 and i % 3 != 0) or i == 3 or i == 2:
                print(i)