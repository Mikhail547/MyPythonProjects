from itertools import product

n = '012345'

for i in product(n, repeat=6): # перебираем всевозможные комбинации слова
    if i[0] == '0' or i[0] == '2':
        continue # пропускаем
    s = ''.join(i)
    if s.count('3') >= 2 and (int(s, 6) + 1) % 2 > 0:
        print(int(s, 6) +1)
        break