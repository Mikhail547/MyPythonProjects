def f(k, c):
    cnt = 0 # считает кол-во букв, карточек которых больше двух и их самих минимум 2
    for i in range(k):
        if c[i] >= 3:
            return True
        if c[i] == 2:
            cnt += 1
    if cnt >= 2:
        return True
    return False

for _ in range(int(input())):
    k = int(input()) # кол-во букв
    c = [int(a) for a in input().split()] # кол-во каждой буквы, а индекс цифр - сама буква, начиная от 'a'eng
    if f(k, c):
        print('YES')
    else:
        print('NO')