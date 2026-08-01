def f(a):
    l = 0
    r = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            l = i
            break
    for i in range(len(a)-1, 0, -1):
        if a[i] < a[i-1]:
            r = i
            break
    return l, r

n = int(input()) # кол-во символов
s = [int(a) for a in input().split()] # испорченный массив
print(*f(s))
