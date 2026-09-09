from matplotlib import rcParams

y = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
k0 = 0
while y >0:
    k0 += int(y%25 ==0)
    y //= 25
print(k0)
    