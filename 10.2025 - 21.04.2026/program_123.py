s = input()
v = 'АВЕКМНОРСТУХ'
if (s[0] in v) and (s[1:4].isdigit()) and (s[4] in v and s[5] in v and s[5] in v) and (s[6] in '_') and ((s[7:].isdigit()) and  2 <= len(s[7:]) <= 3):
    print('YES')
else:
    print('NO')
