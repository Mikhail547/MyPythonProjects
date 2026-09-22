import sys
sys.setrecursionlimit(100000)

def f(n):
    if n >= 17:
        return (n+5) * f(n-9)
    else:
        return 6
print((f(234561) // 436 + f(234552) // 218) // f(234534))