def R(N):
    s = bin(N)[2:]
    if N%3 == 0:
        s += s[-3:]
    else:
       s += bin((N%3)*3)[2:]
    return int(s,2)
print(R(6),R(4)) # 54 19
m = 1
for x in range(1,1000):
    if abs(130- R(x))<= abs(130-R(m)):
        m = x
print(m)
