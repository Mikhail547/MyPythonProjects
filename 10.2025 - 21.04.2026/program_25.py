a = float(input())
b = float(input())
c = float(input())
from math import *
d = b**2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    x0 = -(b /(2 * a))
    print(x0)
elif d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1,x2), sep='\n')