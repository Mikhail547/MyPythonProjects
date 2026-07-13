def R(N):
    s = bin(N)[2:]
    if N % 3 == 0:
        s += s[-3:]
    else:
      s +=  bin((N % 3) * 3)[2:]
    return int(s, 2)
print (R(13), R(4)) # 100 19

m = min(N for N in range(1, 1000) if R(N) >= 200)
print(m)
