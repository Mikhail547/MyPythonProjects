from itertools import product

k = 0
for i in product('акорст', repeat=5):
    k += 1
    if i[0] not in 'аст' and i.count('о') == 2 and k % 2 == 0:
        print(k)
