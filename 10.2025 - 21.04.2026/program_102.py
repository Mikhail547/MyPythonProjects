from math import *
n = input()
if len(n) == 1:
     print(n)
else:
    if len(n) % 2 == 0:
        n_1 = n[0:(len(n) // 2)]
        n_2 = n[-(len(n) // 2):]
    else:
        n_1 = n[0:(floor(len(n)) // 2) + 1]
        n_2 = n[-((len(n)) // 2 ):]
    print(n_2 + n_1)  