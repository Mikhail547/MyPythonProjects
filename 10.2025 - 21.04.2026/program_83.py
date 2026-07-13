n = int(input())
last_digit = 0
summ = 0
while n > 0:
    last_digit = n % 10
    summ += last_digit
    n //= 10
print(summ)