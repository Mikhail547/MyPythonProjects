from itertools import product
k = '01234'

for i in product(k, repeat=5):
    if ''.join(i).count('4') <= 1 and '00' not in ''.join(i):
        print(int(''.join(i), 5) + 1)
        break
print(196*3/8*970/1024) # 11 задание
print(int('100000000000', 2))
#  hhh100000000000hhhh
print(146+191+255+254)
# 7
print(2*56000*8*75/8/1024) # 8204
print(int('10111111', 2))
