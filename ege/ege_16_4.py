F = [3 for n in range(10)]
for n in range(10, 257488):
    F.append((n + 4) * F[n - 5])
print((F[257487]// 683 + 67 * F[257477]) // F[257472])

