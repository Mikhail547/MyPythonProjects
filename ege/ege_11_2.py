from math import *

N = 62 + 10
i = ceil(log2(N))
num_id = ceil(23*1024*1024 / 5_895_222) # байт 1 ид
k = num_id * 8 // i
print(k)