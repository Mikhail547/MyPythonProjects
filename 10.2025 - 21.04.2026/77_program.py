a = int(input())
b = int(input())
max_digit = 0
summ = 0
max_summ = 0
for i in range(a, b +1):
    for j in range(1, b +1):
        if i % j == 0:
            summ += j
            if max_summ == summ:
                if max_digit > i:
                    max_digit = max_digit
                elif max_digit < i:
                    max_digit = i
            if max_summ < summ:
                max_summ = summ
                max_digit = i
            
    summ = 0
print(max_digit, max_summ)

