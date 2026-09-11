def f(a, b): # алгоритм евклида
    if min(a, b) == 0:
        return max(a, b)
    return f(min(a, b), max(a, b) % (min(a, b)))
print(f(25, 60))
print(25*60 / 5)