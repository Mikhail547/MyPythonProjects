def R(N):
    total = ''
    for i in range(len(str(bin(N)))):
        total += bin(N)[-1]
    print(total)
   