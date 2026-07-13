x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + 1 == x2 and y1 == y2) or (x1 - 1 == x2 and y1 == y2) or (x1 == x2 and y1 + 1 == y2) or (x1 == x2 and y1 - 1 == y2) or (x1 + 1 == x2 and y1 + 1 == y2) or (x1 + 1 == x2 and y1 - 1 == y2) or (x1 - 1 == x2 and y1 + 1 == y2) or (x1 - 1 == x2 and y1 - 1 == y2):
    print('YES')
else:
    print('NO') 