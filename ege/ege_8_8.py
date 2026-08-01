from itertools import product

k = 0
for i in product('арсений', repeat=4):
    if i[0] != 'й' and any(a in 'аеи' for a in i):
        k += 1
print(k)

