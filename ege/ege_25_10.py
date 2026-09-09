def P(a): # проверка, простое ли число
    return all(a % d >0 for d in range(2, 1+round(a**0.5)))
def F(x):
    s  = set() # множество простых делителей числа
    for d in range(2, 1 + round(x**0.5)):
        if x % d == 0: # удобная проверка делителя и частного на простоту
            if P(d):
                s.add(d)
            if P(x//d):
                s.add(x//d)

    if len(s) >0 and P(max(s) - min(s)) and\
        str(max(s) - min(s)).count('1') >= 4: # проверка, что у простого числа есть делители, что разница наибольшего и наименьшего делителя числа тоже простая и в этой разнице мин 4 единицы
        return (max(s) - min(s))
    return 0
y, k = 811760076, 0
while k < 5:
    y += 1
    if F(y) != 0:
        print(y, F(y),sep='\t')
        k+=1
