num = int(input())
n = len(str(num))
for i in range(1, n + 1):
    a = (num // 10 ** (n - i)) % 10
    print(a)