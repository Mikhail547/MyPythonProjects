s = input()
s_1 = s.upper()
count = 0
for i in range(len(s)):
    if s[i] != s_1[i]:
        count +=1 
print(count)
