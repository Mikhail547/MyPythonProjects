num = int(input())
n = len(str(num))  # количество цифр

total_summa = 0
total_ymn = 1
one_digit = num // 10**(n - 1)  # первая цифра
summa_digit = num % 10 + one_digit  # последняя цифра
while num != 0:
    total_summa += num % 10  # сумма цирф
    total_ymn  *= num % 10  # произведение цифр
    arifm = total_summa / n  # среднее арифметическое
    num //= 10

print(total_summa, n, total_ymn, arifm, one_digit, summa_digit, sep='\n' )