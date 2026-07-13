n = int(input())
ls = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        ls.append(n//i)
        if n // i == n//(n//i):
            continue
        else:
            ls.append(n//(n//i))
nls = sorted(ls)
print(nls)

