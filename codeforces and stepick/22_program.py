a = float(input())
from math import *
x1 = floor(abs (a))
if a < 0:
    x1 = -x1
else:
    x1 = x1
x2 = ceil(abs(a))
if a < 0:
    x2 = -x2
else:
    x2 = x2
print(x1 + x2)

