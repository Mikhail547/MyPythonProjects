# объявление функции
def print_case_counts(s):
    cnt1 = [a for a in s if a.islower() and a.isalpha()]
    cnt2 = [a for a in s if a.isupper() and a.isalpha()]
    print(f'Букв в верхнем регистре: {len(cnt2)}\nБукв в нижнем регистре: {len(cnt1)}')

# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)
