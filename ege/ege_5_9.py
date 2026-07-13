def F(N):
    s = bin(N)[2:]
    s += str(s.count('1')%2)
    s += str(s.count('1')%2)
    return int(s, 2)
print(F(12), F(7))
m = min(N for N in range(1, 1000) if F(N)>253)
print(m)


