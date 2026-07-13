F = [0, 1]
for n in range(2, 2025):
    F.append(n*F[n-1])
print((F[2024] - 5*F[2023]) // F[2022])
