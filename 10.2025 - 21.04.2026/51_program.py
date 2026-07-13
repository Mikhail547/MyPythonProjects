num = int(input())
n = len(str(num))
digit = 0
flag = True
num_digit = 0
total = 0
for i in range(1, n + 1):
    digit = (num // 10 **(n - i)) % 10
    if digit % 2 == 0:
        num_digit += 1
        total += 1
        print(num_digit, '-я четная цифра равна', sep='', end= ' ')
        print(digit)
if total == 0:
    flag = 'Четных цифр в числе нет'
    print(flag)