b = [int(k) for k in range(12, 35)]
for a in range(10000, 0, -1):
    if all((x%a == 0) or (x % 19 != 0) or (x not in b)  for x in range(1, 10000)):
        print(a)
        break
