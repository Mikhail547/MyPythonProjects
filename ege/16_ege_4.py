import sys

sys.setrecursionlimit(1_000_000_000)

def R(N):
    if N == 1:
        return 1
    elif N > 1:
        return N * R(N - 1)
print((R(3238)// 2 + R(3237))// R(3236))
# 5243940.0
