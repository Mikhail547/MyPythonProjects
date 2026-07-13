def F (a, b):
    if a == b:
        return 1
    if a < b or a == 7:
        return 0
    return F(a-1, b) + F(a - 4, b) + F(a // 3, b)
print(F(19, 13) * F(13, 2))