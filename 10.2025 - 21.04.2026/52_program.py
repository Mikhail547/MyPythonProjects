num = int(input())
n = len(str(num))
digit = 0
flag = 'YES'
for i in range(1, n):
    digit = num % 10
    num //= 10
    maximum = num % 10
    if digit > maximum:
        flag = 'NO'
print(flag)