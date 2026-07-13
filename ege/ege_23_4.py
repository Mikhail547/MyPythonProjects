def F(a, b):
    if a == b:
        return 1
    if a == 7 or a > b:
        return 0
    return F(a + 1, b) + F(a + 3, b) + F(a * 2, b)
print(F(2, 15) * F(15, 25))