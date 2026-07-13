import sys
sys.setrecursionlimit(100_000_000)

def F1(x):
    if x >= 21:
        return F1(x - 8) + 1095
    else:
        return 10 * (G(x - 7) - 36)
def G(x):
    if x >= 22560:
        return x / 23 + 33
    else:
        return G(x + 11) -4
print(F1(548))


