s = input()
l = s.split('.')
flag = 'YES'
for i in range(len(l)):
    l[i] = int(l[i])
    if l[i] > 255:
        flag = ('NO')
        break
print(flag)
