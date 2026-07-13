def F(A):
    for x in range(10000):
        if ((x % 21 == 0) <= ((x % A > 0) <= (x % 77 > 0))) == False:
            return False
    return True
for A in range(1, 10000):
    if F(A) == True:
        print(A)