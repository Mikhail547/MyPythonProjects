def R(N):
    s = bin(N)[2:]
    if N % 5 == 0:
        s += s[-3:]
    else:
        s = bin(N % 5)[2:] + bin(N)[2:]
    return int(s, 2)
print (R(12), R(4))

m = min(N for N in range(1, 1000) if R(N) > 512)
print(m)