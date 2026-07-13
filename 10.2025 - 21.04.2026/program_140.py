s1 = input().lower()
s2 = input().lower()
n1 = 0
n2 = 0
for i in range(len(s1)):
    if s1[i].isalpha():
        n1 += ord(s1[i])
for i in range(len(s2)):
    if s2[i].isalpha():
        n2 += ord(s2[i])
if n1 == n2:
    print('YES')
else:
    print('NO')