from itertools import product

k = '012345'
cnt = 0
for i in product(k, repeat=6):
    if not('0' in i or '1' in i or '2' in i) and i.count('4') == 2 and i.count('5') == 1 and int(''.join(i), 6) + 1 % 2 != 0:
        cnt += 1

print(cnt)