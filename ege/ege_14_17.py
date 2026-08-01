k = '0123456789ABCDEFGHIJKL'

for x in k:
    a = int(f'63{x}89875', 22)
    b = int(f'17{x}51', 22)
    c = int(f'75{x}3', 22)
    if (a + b + c) % 21 == 0:
        print((a + b + c) // 21)
