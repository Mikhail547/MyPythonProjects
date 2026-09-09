A = [[], []]
for s in open('27_A_31163.txt'):
    x, y, t = s.replace(',', '.').split()
    x, y = float(x), float(y)
    if y > x +1:
        A[0].append([x, y])
    else:
        A[1].append([x, y])
B = [[], [], []]
for s in open('27_B_31163.txt'):
    x, y, t = s.replace(',', '.').split()
    x, y = float(x), float(y)
    if y < x and y < 4:
        B[0].append([x, y])
    elif y < -3*x + 16:
        B[1].append([x, y])
    else:
        B[2].append([y, x])
for i in range(len(B[2])):
    k = str(B[2][i]).replace('.', ',')
    k = k[1:-1]

    print(k)



