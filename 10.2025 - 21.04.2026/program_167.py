l = input().split()
l = [int(x) for x in l]
idx_max = l.index(max(l))
idx_min = l.index(min(l))
l[idx_max], l[idx_min] = l[idx_min], l[idx_max]
l = [str(x) for x in l]
print(' '.join(l))


