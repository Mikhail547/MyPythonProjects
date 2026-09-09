def f(a, b): # функция по поиску НОД(наибольший общий делитель a, b)
    if min(a, b) == 0:
        return max(a, b)

    return f(min(a,b), max(a, b) % min(a, b))
print(f(21, 77))
print(77*21/7)