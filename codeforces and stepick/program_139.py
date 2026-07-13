s = ''
max_s = ''
min_s = None

while s != 'КОНЕЦ':

    s = input()
    if min_s == None:
        min_s = s

    if s == 'КОНЕЦ':
        break
    if s > max_s:
        max_s = s

    if s < min_s:
        min_s = s
print(f'Минимальная строка ⬇️: {min_s}\n\
Максимальная строка ⬆️: {max_s}')
