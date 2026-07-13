a = input()
b = input()
c = input()
a1 = len(a)
a2 = len(b)
a3 = len(c)
if (a1 + a2) / 2 == a3:
    print('YES')
elif (a1 + a3) / 2 == a2:
    print('YES')
elif (a2 + a3) / 2 == a1:
    print('YES')
else:
    print('NO')