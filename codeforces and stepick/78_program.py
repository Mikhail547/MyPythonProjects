n = int(input())
counter = 0
counter_1 = n
for i in range(1, n +1):
    for j in range((i // 2) + i):
            counter += 1
            if counter <= i:
                print(counter, end='')
                for d in range((i // 2) + i):
                    counter_1 -= 1
                    print (counter, counter_1, end='')
    counter = 0
    print()
