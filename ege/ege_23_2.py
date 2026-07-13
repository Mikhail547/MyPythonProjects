def F(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return F(a-1, b) + F(a//2, b)
print(F(40, 17)*F(17, 6))
# 56 ответ
