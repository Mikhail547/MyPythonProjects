l = []
for x in '0123456789ABCDEFGHIJKL':
    s = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)
    if s % 21 == 0:
        print(int(x, 22), s / 21)
