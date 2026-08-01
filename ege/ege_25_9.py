def fact(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return [i] + fact(x//i)
    return [x]

for x in range(7_800_001, 7_810_100):
    d = fact(x)
    if len(d) > 1:
        M = max(d) + min(d)
        if M%100 == 63 and M %len(set(d)) == 0:
            print(x, M)

