n = int(input())

for i in range(n):
    s = input()
    if len(s)== 2 and s[0].isdigit() and ord('А')<= ord(s[1])<= ord('П'):
        print('YES')
    else:
        print('NO')
