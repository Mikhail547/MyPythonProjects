from math  import pow 
a_1 = 0
b_1 = 0
e_1 = 0
for a in range(1, 10000):
    a_1 = a
    for b in range(1, 10000):
        b_1 = b
        for c in range(1, 10000):
            for d in range(1, 10000):
                for e in range(1, 10000):
                    e_1 = e
                    if e == pow(a, 3) + pow(b, 3) == pow(c, 3) + pow (d, 3) and e < 10000:
                        print(e_1)