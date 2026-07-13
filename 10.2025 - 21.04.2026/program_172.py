from math import *
def N(R):
    if R % 1 < 0.5:
        return floor(R)
    else:
        return ceil(R)
num = float(input())
print(N(num))

