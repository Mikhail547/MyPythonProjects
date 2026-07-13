with open('point.txt') as f:
    c1, c3, d = [], [], []
    N  = int(f.readline())
    for i in range(N):
        x, y = map(float, f.readline().split())
        c1.append([x, y])
    N = int(f.readline())
    for i in range(N):
        x, y = map(float, f.readline().split())
        c3.append([x, y])
    for p1 in c1:
        for p2 in c1:
            d.append(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5)

    for p1 in c3:
        for p2 in c3:
            d.append(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5)

    m = min(a for a in d if a > 0)
    print(m)