def F(a):
    if a % 9874 == 0:
        print(a, a // 9874, sep='\t')
# 89*6?7?9?
for a in range(10):
    for b in range(10):
        for c in range(10):
            F(89607090 + a*10**4+b*100+c)
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                F(89607090 + a * 10 ** 6 + b * 10**4 + c*100 + d)
for a in range(100):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                F(8900607090 + a * 10 ** 6 + b * 10**4 + c*100 + d)
#8901677598 901527
#8905627198 901927
#8912617990 902635
#8941667298 905577
#8952607690 906685
#8970607992 908508
#8988647790 910335