n = int(input())
total = 0
from math import pow
for i in range(1, n + 1):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        total += i
print(total)
