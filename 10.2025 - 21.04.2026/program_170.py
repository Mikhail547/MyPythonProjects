# объявление функции
def print_sorted_hyphen(s):
    l = s.split('-')
    l.sort()
    print(*l, sep='-')


# считываем данные
s = input()

# вызываем функцию
print_sorted_hyphen(s)