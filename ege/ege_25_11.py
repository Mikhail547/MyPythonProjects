from math import *
def P(a): # проверка, простое ли число
    return all(a % d >0 for d in range(2, isqrt(a)+1))
def F(x):
    s  = set() # множество простых делителей числа
    for d in range(2, isqrt(x) + 1):
        if x % d == 0: # удобная проверка делителя и частного на простоту
            if P(d) and str(d).count('16') == 1 and  P(x//d) and str(x//d).count('16') == 1 and x == d * (x//d):
                s.add(d)
                s.add(x//d)
    if len(s) > 0:
        return min(s)
    return 0

cnt = 0
n = 1_104_285_718

while cnt < 5:
    if F(n) != 0:
        print(n , F(n), sep='\t')
        cnt += 1
    n += 1