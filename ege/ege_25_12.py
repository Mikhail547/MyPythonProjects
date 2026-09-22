def Pr(a): # проверка, что число простое
    return all( a % d > 0 for d in range(2, round(a**0.5)+1))

def f(x):
    s = set()  # множество простых делителей числа
    for d in range(2, round(x**0.5)+1):
        if x % d == 0:
            if Pr(d) and Pr(x//d) and str(d).count('3') == 2 and str(x//d).count('3') == 2:
                s.add(d)
                s.add(x//d)
    if len(s) >0:
        return max(s)
    return 0

k = 8_996_453
cnt = 0
while cnt < 5:
    if f(k) >0:
        print(k, f(k))
        cnt += 1
    k += 1

