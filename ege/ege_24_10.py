import sys

sys.set_int_max_str_digits(100000)

with open('24_31343.txt') as f:
    s = f.readline().strip()

# Шаг 1: Заменяем все запрещенные комбинации знаков на пробелы
for bad in ['++', '**', '+*', '*+', '*0', '+0']:
    s = s.replace(bad, ' ')

# Шаг 2: Убираем нули, перед которыми нет цифры
s_list = list(' ' + s)
for i in range(1, len(s_list)):
    if s_list[i] == '0' and not s_list[i - 1].isdigit():
        s_list[i] = ' '

clean_string = ''.join(s_list)
expressions = clean_string.split()

max_len = 0

# Шаг 3: Перебираем куски с олимпиадным ускорением!
for expr in expressions:
    expr = expr.strip('+*')
    if not expr:
        continue

    for i in range(len(expr)):
        # ТРЮК: стартуем только с той длины, которая БОЛЬШЕ нашего рекорда!
        for j in range(i + max_len, len(expr)):
            sub_expr = expr[i: j + 1]

            # Быстрая проверка краев
            if sub_expr[0] not in '+*' and sub_expr[-1] not in '+*':

                # Если нашли ведущий ноль в начале — дальше расширять БЕСПОЛЕЗНО
                if sub_expr[0] == '0' and len(sub_expr) > 1:
                    break  # Выходим из цикла j, смещаем левый указатель i

                # Запускаем eval() только для потенциальных рекордсменов!
                if eval(sub_expr) % 2 == 0:
                    max_len = max(max_len, len(sub_expr))

print(max_len)

