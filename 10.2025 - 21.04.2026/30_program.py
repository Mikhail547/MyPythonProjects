n = int(input())
a = 0
from math  import log
for i in range(1, n + 1):
    a += 1 / (i)
print( a - log(n))
