F = [0, 1]
for n in range(2, 17300):
    F.append((n-1)*F[n-1])
print((F[17258]+3*F[17257]) / F[17256])
