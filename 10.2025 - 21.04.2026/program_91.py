n = input()
for i in range(1, len(n) + 1):
    print(str(i) + ')', end=' ')
    for j in range(1):
        print(n[i - 1])