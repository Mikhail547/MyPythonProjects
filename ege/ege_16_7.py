import sys
sys.setrecursionlimit(10000000)

def f(n):
    return 3 *g(n -3) + 7
def g(n):
    if n > 20:
        return g(n-3) + 1
    else:
        return n + 2
print(f(37811))