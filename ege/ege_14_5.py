m = 2030
for x in range(1, 2031):
    y = 6**2030 + 6**100-x
    k = 0
    while y> 0:
        k += int(y %6 ==0)
        y//= 6
    m = min(m,k)
print(m)
