def f(a):
    for x in range(70, 91):
        if x % 16 == 0 and x % a == 0:
            return True

for a in range(1, 100):
    if f(a):
        print(a)
