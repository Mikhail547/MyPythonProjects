def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '11' + s + '11'
    else:
        s = '1' + s + '00'
    return int(s, 2)

print(f(13), f(6))

m = min( f(a) for a in range(1, 1000) if f(a) > 95)
print(m)