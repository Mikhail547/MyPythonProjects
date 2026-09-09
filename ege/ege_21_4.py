def f(k, s, n):
    if k + s <= 53: # если кто-то победил, проверка, победил ли это ваня
        return n == 4
    if n == 4: # на второй ход вани он так и не выйграл
        return False
    if n % 2 == 0:
        return all([f(k - 3, s, n + 1), f(k, s - 3, n + 1), f(k // 3, s, n + 1), f(k, s // 3, n + 1)]) # ход пети
    return any([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)]) # ход вани

def f1(k, s, n):
    if k + s <= 53: # если кто-то победил, проверка, победил ли это ваня
        return n == 2
    if n == 2: # на первый ход вани он так и не выйграл
        return False
    if n % 2 == 0:
        return all([f(k - 3, s, n + 1), f(k, s - 3, n + 1), f(k // 3, s, n + 1), f(k, s // 3, n + 1)]) # ход пети
    return any([f(k-3, s, n+1), f(k, s-3, n+1), f(k//3, s, n+1), f(k, s//3, n+1)]) # ход вани

for s in range(35, 1000):
    if f(19, s, 0) and not(f1(19, s, 0)):
        print(s)
        break