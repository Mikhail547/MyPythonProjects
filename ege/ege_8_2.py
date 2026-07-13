from itertools import product

# Цифры семеричной системы счисления: 0, 1, 2, 3, 4, 5, 6
digits = "0123456"
count = 0

# Генерируем все возможные пятизначные комбинации цифр
for num_tuple in product(digits, repeat=5):
    # Пятизначное число не может начинаться с нуля
    if num_tuple[0] == "0":
        continue

    # Считаем количество нулей и единиц в числе
    zeros = num_tuple.count("0")
    ones = num_tuple.count("1")

    # Проверяем условия задачи: ровно один ноль и не более двух единиц
    if zeros == 1 and ones <= 2:
        count += 1

print(f"Количество таких чисел: {count}")
