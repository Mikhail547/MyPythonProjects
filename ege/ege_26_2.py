def f(i, j, k):
    if abs(i - j) <= k:
        return True
    else:
        return False
s = [int(a) for a in open('26_31162.txt')]
cnt_d = 0
m = s.index(max(s))
n = 14931
a = 118
b = 201
l = set()
for i in range(m, len(s)): #  количество уникальных продуктов
    if a <=s[i] <= b and f(s[i], s[i+1], 5):
        cnt_d += 1
        l.add(s[i])
s.sort()
s = s[::-1]
for i in s: # наивысшее возможное место в рейтинге товаров
    if i in l:
        print(s.index(i)+1)
        break

print(cnt_d)
