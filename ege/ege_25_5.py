def F(x):
    if x < x:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def F1(x):
    if str(x).count('3') == 2:
        return True
    else:
        return False

N = 8_996_452
cnt = 0
n1 = N +1
while cnt < 5:
    for i in range(2, int(n1**0.5) + 1):
        if n1 % i == 0:
            s1 = i
            s2 = n1 // i
            if (F(s1) and F1(s1) and F(s2) and F1(s2)) == True:
                print(n1, max(s1, s2))
                cnt += 1
                break
    n1 += 1




