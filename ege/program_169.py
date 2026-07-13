numbers = input().split()
numbers = [int(s) for s in numbers]
total = sum(numbers)

# Перебираем все элементы, кроме последнего
for num in numbers[:-1]:
    print(num, end="+")

# Последний элемент выводим отдельно со знаком "=" и результатом
print(f"{numbers[-1]}={total}")

