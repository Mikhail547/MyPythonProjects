
s = input()
s_0 = ''
last_spase = 0
ss = ''
sl = ''
if s[0].isalpha() == 0:
    ss = s[0]
    s[0].replace('"','')
if s[-1].isalpha() == 0:
    sl = s[-1]
    s[-1].replace('"', '')
for i in range(len(s)):
    if s[i].isspace():
        if last_spase == 0:
            s_0 += s[i::-1]
            last_spase = i
        s_0 += s[i:last_spase:-1]
        last_spase = i
    if s[i] == s[-1]:
        s_0 +=' ' + s[i:last_spase:-1]
print(ss + s_0.strip() + sl)

