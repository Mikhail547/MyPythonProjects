n = int(input())
s = input()
s1= ''
for i in range(len(s)):
    if ord('a') <= ord(s[i]) - n <= ord('z'):
        s1 +=  chr(ord(s[i]) -n)
    if ord('a') > ord(s[i]) - n:
        s1 += chr(ord('a') +(26 - (ord('a') - (ord(s[i]) - n))))
print(s1)

