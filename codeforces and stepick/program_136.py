from itertools import count

s = input()
i = 0

while s.count('-1') > 0:
    if s[i].isdigit() ==  1:
        n = chr(int(s[i: i + 4]))
        s = s.replace(s[i-3:i +5 ], n)
    i += 1
print(s)


