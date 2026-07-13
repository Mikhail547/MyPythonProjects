for i in ('0123456789ABCDEFGHIJKLM'):
    if (int(f'761{i}035', 23) + int(f'338{i}932', 23)) % 22 == 0:
        print((int(f'761{i}035', 23) + int(f'338{i}932', 23)) / 22)
