def f(s, k, p, fin):
    if s + k >= 136:
        return p in fin
    if p >= max(fin):
        return False
    moves = [f(s+3, k, p+1, fin),f(s, k+3, p+1, fin), f(s*2, k, p+1, fin), f(s, k*2, p+1, fin)]
    return any(moves) if ((p+1) % 2) == (fin[0] % 2) else all(moves)
print([s for s in range(1, 127) if f(s, 9, 0, [2])]) # 32
print([s for s in range(1, 127) if f(s, 9, 0, [3])])
print([s for s in range(1, 127) if f(s, 9, 0, [2, 4]) and not f(s, 9, 0, [2])])