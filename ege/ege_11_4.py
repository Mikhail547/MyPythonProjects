from math import *
k = 2783
id = ceil(11 * 1024 * 1024 * 1024 / 3_845_627)
i = ceil(id * 8 / k) # бит на 1 символ

print(2**(i-1)+1)
