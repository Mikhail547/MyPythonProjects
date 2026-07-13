n = int(input())
l = []
for i in range(n):
    l.append(input())
L = []
k = int(input())
cnt = 0
for i in range(k):
    L.append(input())
for i in l:
    for j in L:
        if j.lower() in i.lower():
            cnt += 1
            if cnt == k:
                print(i)
    cnt = 0
