def f(a, b):
    if a % b == 0:
        return 0
    if a < b:
        return b - a
    return b - (a % b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f(a, b))


