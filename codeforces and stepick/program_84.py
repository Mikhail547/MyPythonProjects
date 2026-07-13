count = 0
maximum = 10 ** 12
max_digit = 0
for i in range(1, 8 + 1):
    num = int(input())
    if len(str(num)) > 12:
        continue
    if num % 4 == 0:
        count += 1
    if max_digit < num < maximum:
        max_digit = num
if count > 0:
    print(count)
    print(max_digit)
else:
    print('NO')