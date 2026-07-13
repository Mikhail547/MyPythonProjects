num_1 = int(input())
num_2 = int(input())
counter = 0
for i in range(num_1, num_2 +1):
    for j  in range(1, num_2 +1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
    counter = 0