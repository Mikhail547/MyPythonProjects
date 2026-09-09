def f(a):
    if all((x + y <= 27) or (y <= x -1) or (y >= a) for x in range(10000) for y in range(10000)):
        return a
for a  in range(1000, 0, -1):
    if f(a):
        print(a)
        break