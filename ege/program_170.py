l = input().split()
l = [int(s) for s in l]
m = sum(l)
for n in l[:-1]:
    print(n, end='+')

print(f'{l[-1]}={m}')

