def R(N):
    l = []
    for i in range(n):
        s = input().split()
        l.extend(s)
    l = [int(a) for a in l ]
    l.sort()
    l = [str(a) for a in l ]

    d = (' ').join(l)
    return d



n = int(input())
print(R(n))
