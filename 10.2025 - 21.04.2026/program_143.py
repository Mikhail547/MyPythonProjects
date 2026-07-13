n = int(input())
s_l = input()
flag = 'YES'

for i in range(n-1):
    s = input()
    if s[:s.find(' ')] < s_l[:s_l.find(' ')]:
        flag = 'NO'
    if s[:s.find(' ')] == s_l[:s_l.find(' ')]:
        if s[s.find('«'):s.find('»')] < s_l[s.find('«'):s_l.find('»')]:
            flag = 'NO'
    s_l = s
print(flag)
