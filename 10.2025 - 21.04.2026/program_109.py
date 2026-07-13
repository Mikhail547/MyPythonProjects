s = input()
count_1, count_2, count_3, count_4 = 0, 0, 0, 0
for i in range(len(s)):
    if 'а' in s.replace('А', 'а')[i]:
        count_1 += 1 
    if 'г' in s.replace('Г', 'г')[i]:
        count_2 += 1 
    if 'ц' in s.replace('Ц', 'ц')[i]:
        count_3 += 1 
    if 'т' in s.replace('Т', 'т')[i]:
        count_4 += 1 
print('Аденин:', count_1)
print('Гуанин:',count_2)
print('Цитозин:',count_3)
print('Тимин:', count_4)
