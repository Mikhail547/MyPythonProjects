def f(a):
    cnt = 0
    for i in range(2, int(a**0.5)+ 1):
        if a % i == 0:
            return False
    return True
def r(a):
    if '67' in str(a) and str(a).count('67') == 1:
        return True
    else:
        return False

N = 2_626_695_891
n = N + 1

cnt = 0
while cnt < 5:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s1 = i
            s2 = n // i
            if f(s1) and f(s2) and r(s1) and r(s2):
                cnt += 1
                print(n, min(s1, s2))
                break
    n += 1


