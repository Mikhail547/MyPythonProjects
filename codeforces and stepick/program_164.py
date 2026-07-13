s = input().lower()
l = s.split()
cnt = 0
while 'a' in l:
    l.remove('a')
    cnt += 1
while 'an' in l:
    l.remove('an')
    cnt += 1
while 'the' in l:
    l.remove('the')
    cnt += 1
print(f'Общее количество артиклей: {cnt}')


