s = input()
if s.count('f') > 0 :
    if s.count('f') == 1:
        print(s.find('f'))
    if s.count('f') > 1:
        print(s.find('f'), s.rfind('f'))
else:
    print('NO')
