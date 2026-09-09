def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if '1' in str(a):
        c = int(str(a).replace('1', '3'))
        return f(a+1, b) + f(c, b)
    return f(a+1, b)
print(f(10, 84))