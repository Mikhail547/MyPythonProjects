num = int(input())
n = len(str(num))
for _ in range(1, n +1):
    digit = num // 10 ** (n - 2) % 10
print(digit)