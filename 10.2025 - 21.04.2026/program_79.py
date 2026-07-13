n = int(input())
counter = 0
counter_1 = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        counter += 1
        print(counter, end="")
    else:
        for z in range(1):
            counter_1 = i -1
            while counter_1 > 0:
                print(counter_1, end='')
                counter_1 -= 1
    counter = 0
    print()
