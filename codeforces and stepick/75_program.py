n = int(input())
f = 1
s = 0
for i in range(1, n +1):
    for j in range(1, i +1):
        f *= j
    s += f
    f = 1
print(s)