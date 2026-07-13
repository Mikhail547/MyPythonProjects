num = int(input())
n = len(str(num))
m = 1
for i in range(n):
    digit = (num % 10 **(m)) // 10 ** i
    m += 1
    print(digit, end='')