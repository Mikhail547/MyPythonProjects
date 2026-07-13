def f3(a):
    s3 = '' 
    while a > 0:
        s3 += str(a % 3)
        a //= 3
    return s3[::-1] 
def R(N):
    s = f3(N)
    if N % 3 == 0:
        s += s [-2:]
    else:
        s += f3( sum(map(int, s)) * 3 )
    return int(s, 3)
print(R(8), R(9))
m = min(R(a) for a in range(1, 1000) if R(a) > 208 and R(a) % 2 > 0)
print(m)
