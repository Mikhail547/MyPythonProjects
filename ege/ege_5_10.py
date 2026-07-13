def R(N):
    s = bin(N)[2:]
    if N % 2 == 0:
        s = '11' + s + '11'
    else:
        s = '1' + s + '00'
    return int(s, 2)
print(R(13))
l = []
m = 0
for i in range(1, 114):
    if R(i) < 113:
        l.append(R(i))



print(max(l))


