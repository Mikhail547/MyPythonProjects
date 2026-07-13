s = input()
s = s.replace('+', '')
l = []
l.extend(s)
l.sort()
for i in range(len(l)):
    if i < len(l)-1:
        print(l[i], end='+')
    else:
        print(l[i])







