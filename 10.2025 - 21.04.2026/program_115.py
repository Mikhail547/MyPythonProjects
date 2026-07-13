with open('17_25356.txt') as f:
    x = [int(a) for a in f]
    y = []
    m30 = max(a for a in x if abs(a) % 100 == 30)
    for i in range(len(x) -2):
        k = len([a for a in x[i:i + 3] if 10 **3 <=abs(a) if 10 ** 3 <= abs(a)< 10** 4])
        if k == 0 and sum(x[i:i+3]) > m30:
            y.append(sum(x[i:i + 3]))

print(len(y), max(y))