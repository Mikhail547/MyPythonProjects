for x in '0123456789ABCDE':
    s = int(f'97968{x}15', 15) + int(f'7{x}233', 15)
    if s % 14 == 0:
        print(x, s // 14)