for a in range(50, 21, -1):
    if all(a or (b != c) for b in range(22, 41) for c in range(32, 51)):
        print(a)
