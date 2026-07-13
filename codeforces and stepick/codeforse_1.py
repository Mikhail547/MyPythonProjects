s = input()
sn = ''

for i in range(len(s)):
    sn += s[i]

    if s.count(s[i])>1 and s[i].isspace() == 0:
        s = s.replace(s[i], ' ')
sn = sn.replace(' ', '')

if len(sn) % 2 == 0:
    print('CHAT WITH HER!')
else:

    print('IGNORE HIM!')