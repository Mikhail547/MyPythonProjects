num = 113
x = 1
while num < 2026:
    if (num % 2 != 0) and (num % 10 != 5):
        x *= num
        print(num)
    num += 1
print(x)

