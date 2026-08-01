from math import *
n = 10+4090 # всего символов
i = ceil(log2(n)) # бит на символ
id = ceil(101 * i / 8) # байт один номер
ans = (2048 * id / 1024) # кбайт
print(ans)

