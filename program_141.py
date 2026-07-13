s1 = input()
s2 = input()
s3 = input()
d = ''
for i in range(1):

    if min(s1,s2,s3)< s1 < max(s1,s2,s3):
        d = s1
    if min(s1,s2,s3)< s2 < max(s1,s2,s3):
        d = s2
    if min(s1,s2,s3)< s3 < max(s1,s2,s3):
        d = s3
print(min(s1,s2,s3),max(s1,s2,s3), d)