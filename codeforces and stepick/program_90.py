n = ''
for i in range(3):
    name = input()
    n = n + name[0]
else:
    for j in range(1, -2, -1):
        print(n[j], end='')