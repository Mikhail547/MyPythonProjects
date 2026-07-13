def R(N):
    l = []
    l1= []
    l.extend(N)
    l[::-1]
    for i in range(0, len(l)):
        if l[i] not in l1:
            l1.append(l[i])

    return l1

l = eval(input())
print(R(l))
