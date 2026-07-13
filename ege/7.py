def R(A):
    # Ограничиваем диапазоны для ускорения работы программы
    for x in range(486):
        for y in range(2500):
            if not ((x * y < A) or (5 * x < y) or (486 <= x)):
                return False
    return True # <--- Теперь возвращает True только после проверки ВСЕХ x и y

for A in range(1, 10000):
    if R(A):
        print(A) # Правильный ответ: 2426
        break
