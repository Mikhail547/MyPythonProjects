s = input()
count = 0
max_n = 0
max_s = ''
for i in range(len(s)):
    if s.count(s[i]) >= max_n:
        max_n = s.count(s[i])
        max_s = s[i]
print(max_s, max_n)