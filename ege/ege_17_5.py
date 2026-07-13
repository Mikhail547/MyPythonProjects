x =[int(a) for a in open('17_ege_23_6.txt')]
y = []
m = max(a for a in x if a % 100 == 28)


for i in range(len(x) - 2):
    if (100 <= abs(x[i]) <= 999 or 100 <= abs(x[i + 1]) <= 999 or 100 <= abs(x[i + 2]) <= 999)\
            and 0 < sum(x[i:i+3]) /3 < m:
        y.append(sum(x[i:i+3]))
print(len(y), max(y))
