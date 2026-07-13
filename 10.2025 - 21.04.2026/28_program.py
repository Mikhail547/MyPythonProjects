a = int(input())
b = int(input())
counter = 0
from math import pow
for i in range(a, b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        counter += 1
print(counter)
