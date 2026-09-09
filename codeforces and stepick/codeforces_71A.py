def f(a):
    if len(a) > 10:
        s = f'{a[0]}{len(a)-2}{a[-1]}'
        return s
    return a

for _ in range(int(input())):
    print(f(input()))
