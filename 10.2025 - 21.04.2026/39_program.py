n = int(input())
largest1 = 1
largest2 = 0
print(1, end=' ')
for _ in range(n - 1):
    if n == 1:
        break
    total = largest1 + largest2
    print(total, end=' ')
    largest2 = largest1
    largest1 = total 