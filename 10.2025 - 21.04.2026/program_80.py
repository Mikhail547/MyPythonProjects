num = int(input())
counter = 0
for i in range(1, num + 1):
        for j in range(i):
            counter += 1
            print(counter, end=' ')
        print()