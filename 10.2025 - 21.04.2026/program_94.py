w = input()
count_1 = 0
count_2 = 0
digit = '+'
digit_2 = '*'
for c in w:
    if c in digit:
        count_1 += 1
    if c in digit_2:
        count_2 += 1
print('Символ + встречается', count_1, 'раз')
print('Символ * встречается', count_2, 'раз')