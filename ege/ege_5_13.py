def f(a):
    s = ''
    while a > 0:
        s += str(a % 3)
        a //= 3
    return s[::-1]

def f1(n):
    if n % 3 == 0:
        s = '1' + f(n) + '02'
    else:
        s = f(n) + f(n%3*5)
    return int(s, 3)

for i in range(1, 178):
    if f1(i) > 177:
        print(i)
        break




