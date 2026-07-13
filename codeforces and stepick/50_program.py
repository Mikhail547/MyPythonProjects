num = int(input())
flag = 'YES'
maximum = 0
minimum = 9

while num != 0:
    if num % 10 > maximum:
        maximum = num % 10
    if num % 10 < minimum:
        minimum = num % 10
    if maximum != minimum:
        flag = 'NO'
    num //= 10
print(flag)