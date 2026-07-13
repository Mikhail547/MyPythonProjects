def R(N):
    s = bin(N)[2:]
    if N%2 == 0:
        s = '10' + s
    else:
       s = '1' + s + '01'
    return int(s,2)

m = min(R(N) for N in range(1000) if N> 18)
print(m)

