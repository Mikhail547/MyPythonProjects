def R(N):

    s = bin(N)[2:]
    while 1 == True:
        if N % 5 == 0:
            s += bin(5)[2:]
        else:
            s += '1'
        if int(s, 2) % 7 == 0:
            s += bin(7)[2:]
        else:
            s += '1'
        if N < 1728404:
            break
        return
print(R(10))