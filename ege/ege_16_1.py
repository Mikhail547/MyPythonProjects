G = [2*n for n in range(10)] # ищем значение через массив
for n in range(10, 16000):
    G.append(G[n-2] + 1)
F = [2 * (G[n - 3 ] + 8) for n in range(16000)]
print(F[15548])
