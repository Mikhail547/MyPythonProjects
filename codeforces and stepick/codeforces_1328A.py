def f(a, b):
    b_b = set()
    for i in range(1, int(b**0.5)+1):
        if b % i == 0:
            if a <= b % i:
                b_b.add(i)
            if a <= b//i:
                b_b.add(b//i)
    k = list(b_b)
    k.sort()
    if len(k) >0:
        if a == k[0]:
            return a
        else:
            return k[0] - a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f(a, b))
# код полностью неправильный, но он мне нравится, поэтому удалять не буду

