a = int(input())
if (1000 <= a >= 9999 and a % 1000 % 100 == 00) or (100 <= a >= 999 and a % 100 == 00):
    print('YES')
else:
    print('NO')

