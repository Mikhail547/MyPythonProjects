G = [(n/20 + 28) for n in range(250000)]
for n in range(248044, -1, -1):
    G[n] = G[n + 9] - 4
F= [6 * (G[n-7] - 36) for n in range (19)]
for n in range(19, 674):
    F.append(F[n - 4] + 3580)
print(F[673])
