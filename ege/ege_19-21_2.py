def g(s, p, end):
    if s <= 30: return p in end
    if p >= max(end): return False
    moves = [g(s-3, p+1, end), g(s//4, p+1, end), g(s-5, p+1, end)]
    return any(moves) if ((p+1) % 2 ) == (end[0] % 2) else all(moves)
print([s for s in range(31, 1000) if g(s, 0, [2])])
print([s for s in range(31, 1000) if g(s, 0, [3])])
print([s for s in range(31, 1000) if g(s, 0, [2, 4]) and not g(s, 0, [2])])


