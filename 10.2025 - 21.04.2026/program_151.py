n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
for num in l:
    if num < 0:
        print(num)
for num in l:
    if num == 0:
        print(num)
for num in l:
    if num > 0:
        print(num)
