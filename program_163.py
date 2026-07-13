s = input()
l = s.split()
cnt = 0
for i in range(len(l)):
    if l[i] == '':
        continue
    cnt += l.count(l[i]) - 1
    l[i] = ''
print(cnt)
