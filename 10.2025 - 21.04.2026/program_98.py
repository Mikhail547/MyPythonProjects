from math import *
n_10 = int(input())
n_2 = ''
while n_10 > 0:
    if n_10 % 2 == 0:
        n_2 += '0'
    else:
        n_2 += '1'
    n_10 //= 2
x = ''
y = len(n_2) - 1 
for i in range(0,len(n_2)):
    x += n_2[y - i]
print(x)
