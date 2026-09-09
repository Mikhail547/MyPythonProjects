import sys
sys.setrecursionlimit(1_000_000)
def f(a):
    if a == 1:
        return 1
    else:
        return (a -1) * f(a -1)
print((3*f(32028)-f(32027))/ f(32026))
