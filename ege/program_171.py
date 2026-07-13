l = input().split('-')
flag = 'NO'
if len(l) == 4 and len(l[0]) == 1 and l[0] == '7' and len(l[1]) == 3 and len(l[2]) == 3 and len(l[3]) == 4 and ''.join(l).isdigit():
    flag =  'YES'
if len(l) == 3 and len(l[0]) == 3 and len(l[1]) == 3 and len(l[2]) == 4 and ''.join(l).isdigit():
    flag = 'YES'
print(flag)

