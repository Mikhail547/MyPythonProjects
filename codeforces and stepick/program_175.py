def R(N, M):
    l = []
    l.extend(N)

    if M in l:

        x = l[::-1].index(M)
        return len(l)-1 - x
    else:
        return 'ERROR!'

n = eval(input())
s = eval(input())
print(R(n,s))

