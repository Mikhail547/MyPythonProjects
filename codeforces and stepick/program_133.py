s = input()
bee = 0
bee2 = 0

ru = 'еуорахсЕТОРАНХСВМ'
eng = 'eyopaxcETOPAHXCBM'
for i in range(len(s)):
    bee += ord(s[i]) * 3
    if s[i] not in eng:
        bee2 += ord(s[i]) * 3
    for j in range(len(eng)):
        if s[i] == eng[j]:
            bee2 += ord(ru[j]) * 3
        
print(f'Старая стоимость: {bee}🐝\n\
Новая стоимость: {bee2}🐝')