s = input()
a, b = int(s[:s.find(' ')]), int(s[s.find(' ')+1:])
cnt = 0
while a <= b:
    cnt += 1
    a *= 3
    b *= 2
print(cnt)
