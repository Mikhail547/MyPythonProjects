n = int(input())
last_digit = 0
x = len(str(n))
while x > 1:
    summ = 0
    while n > 0:
        last_digit = n % 10
        summ += last_digit
        n //= 10
    n = summ
    x = len(str(n))
print(n)
