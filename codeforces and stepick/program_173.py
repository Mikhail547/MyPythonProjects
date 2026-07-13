def R(N):
    l = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            l.append(N // i)
            if N //(N//i) not in l:
                l.append(N //(N//i))


    l.sort()
    return len(l)
n = int(input())
print(R(n))

