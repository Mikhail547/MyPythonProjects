def F(a, b):
    if a == b:
        return 1
    if a < b or a == 73:
        return 0
    return F(a -3, b) + F(a - 8, b) + F( a // 2, b)
print(F(76, 41)* F(41, 12))

