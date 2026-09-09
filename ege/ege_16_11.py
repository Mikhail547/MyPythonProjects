f = [0, 1]

for n in range(2, 3039):
    f.append(n*f[n-1])
print((f[3038] + 5*f[3037]) / f[3036])