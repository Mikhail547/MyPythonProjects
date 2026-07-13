num = int(input())
counter = 0
for i in range(1, num + 1):
    for j in range(1, num +1):
        if i % j == 0:
            counter += 1
    print(i, counter * '+', sep='')
    counter = 0
