n = int(input())
counter_3  = 0
counter_10 = 0
counter_2 = 0
total_5 = 0
multi_7 = 1
counter_0 = 0
counter_5 = 0
counter_05 = 0
last_digit = n % 10
while n > 0:
    if n % 10 == 3:
        counter_3 += 1
    if n % 10 == last_digit:
        counter_10 += 1
    if (n % 10) % 2 == 0:
        counter_2 += 1
    if n % 10 > 5:
        total_5 += n % 10
    if n % 10 > 7:
        multi_7 *= n % 10
    if n % 10 == 0:
        counter_0 += 1
    if n % 10 == 5:
        counter_5 += 1
    n //= 10
counter_05 = counter_5 + counter_0
print(counter_3, counter_10, counter_2, total_5, multi_7, counter_05, sep='\n')