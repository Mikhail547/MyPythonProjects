x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - 1 == x2 and (y1 - 1 == y2 or y1 + 1 == y2 or y1 == y2):
    print("YES")  # шаг инвалидной коляски
elif x1 == x2 and (y1 - 1 == y2 or y1 + 1 == y2 or y1 == y2):
    print("YES")
elif x1 + 1 == x2 and (y1 - 1 == y2 or y1 + 1 == y2 or y1 == y2):
    print("YES")
elif x1 == x2 or y1 == y2:  # тот что самый крайний по диагонали и горизонтали только
    print("YES")
elif x1 - x2 == y2 - y1 or x1 - y1 == x2 - y2:  # слон
    print("YES")
else:
    print("NO")
