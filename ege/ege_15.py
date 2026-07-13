def F(A):
    for x in range(1, 25*60 +1):
        if ((x%25 == 0) <= ((x % A > 0) <= (x%60>0))) == False:
                return False
    return True
for A in range(1, 25*60+1):
    if F(A) == True:
        print(A)
        