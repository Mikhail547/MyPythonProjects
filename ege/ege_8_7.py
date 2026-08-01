from itertools import product

k = 0
for x in product('БАЛОН', repeat=6):
    if x.count('А') <= 1 and x.count('О') <= 1:
        k += 1
print(k)
