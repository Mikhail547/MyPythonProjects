def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a//10%10 < a%10:
        c = list(str(a).strip())
        c[1], c[2] = c[2], c[1]
        k = int(''.join(c))
        return f(a+1, b) + f(k, b)
    return f(a+1, b)
print(f(112, 165))