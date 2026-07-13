# объявление функции
def print_symbol_counts(s):
    l = []
    ln = []
    for i in s:

        k = i + ': '
        if k in l:
            continue
        l.append(k)
        ln.append(str(s.count(i)))
        d = []
    for i in range(len(l)):
        d.append(l[i] + ln[i])
        d.sort()
    print(*d, sep='\n')


# считываем данные
s = input().lower()

# вызываем функцию
print_symbol_counts(s)