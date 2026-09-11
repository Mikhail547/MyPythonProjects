def f(a, b):
    if a % b == 0:
        return True
    else:
        return False
p = [int(a) for a in range(2508, 2571)]
for a in range(10_000, 0, -1):
    if all(f(x, a) or not(x in p) or not(f(x, 214)) or (x + a <= 5286) for x in range(5000)):
        print(a)
        break
