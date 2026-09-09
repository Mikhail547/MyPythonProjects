k = 0
for _ in range(int(input())):
    s = [a for a in input() if not (a.isspace())]
    n = ''.join(s)
    if n.count('1') >= 2:
        k += 1
print(k)

