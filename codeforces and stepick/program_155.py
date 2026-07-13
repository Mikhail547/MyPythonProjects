n = int(input())
l = []
for i in range(n):
    l.append(input())
s = input()
for i in l:
    if s.lower() in i.lower():
        print(i)