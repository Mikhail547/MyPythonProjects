n = int(input())
total = 0
for i in range(len(str(n))):
    total += n % 10
    n //= 10
print(total)