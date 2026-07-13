n = int(input())
largest1 = 0
largest2 = 0
for i in range(1, n +1):
    num = int(input())
    if largest2 < num < largest1:
        largest2 = num
    if num > largeast1:
        largest2 = largest1
        largeast1 = num
print(largest1, largest2, sep='\n')
