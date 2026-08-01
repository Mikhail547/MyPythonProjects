import itertools
from itertools import permutations
def f(k, c):
    x = []
    for i in range(k):
        x.append(chr(ord('a')+i)*c[i])
    s = ''.join(x)
    cnt = 0
    for i in itertools.permutations(s):
        for j in range(len(i)-1):
            x = i[j:j+2]
            cnt = 0
            for y in range(len(i)-1):
                if x == i[y:y+2]:
                    cnt += 1
            if cnt > 1:
                return True
    return False

for _ in range(int(input())):
    k = int(input()) # кол-во букв
    c = [int(a) for a in input().split()] # кол-во каждой буквы, а индекс цифр - сама буква, начиная от 'a'eng
    if f(k, c):
        print('YES')
    else:
        print('NO')
# проверил, код, он правильный, но работает только на небольших числах, для ответа на олимпиаде не подойдёт