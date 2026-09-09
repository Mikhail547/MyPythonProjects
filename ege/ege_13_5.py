def f(a, b):
    if a == b:
        return 1
    if a >b:
        return 0
    if (a//10)%10 < a%10:
        c = int(str(a)[0] + str(a)[2] + str(a)[1])
        return f(c, b) + f(a+1, b)
    return f(a+1, b)
print(f(100, 141))