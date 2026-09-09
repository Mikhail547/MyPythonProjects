def f(s1, s2, p, end):
    if s1 + s2 <= 53: return p in end
    if p >= max(end): return False

    m = [f(s1-3, s2, p+1, end), f(s1//3, s2, p+1, end), f(s1, s2//3, p+1, end), f(s1, s2-3, p+1, end)]

    return any(m) if ((p + 1) % 2) == (end[0] % 2) else all(m)

print([s for s in range(35, 1000) if f(19, s, 0, [2])])
print([s for s in range(35, 1000) if f(19, s, 0, [3])])
print([s for s in range(35, 1000) if f(19, s, 0, [2, 4]) and not f(19, s, 0, [2])])