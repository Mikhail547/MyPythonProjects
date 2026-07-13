num = int(input())  # 31256
a = num % 10  # 6
b = (num % 100) // 10  # 12, = 5
c = num % 1000 // 100
d = num // 1000 % 10
e = num // 10000
print(a, b, c, d, e)
