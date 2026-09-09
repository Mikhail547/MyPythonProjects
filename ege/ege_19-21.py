def g(s, p, end):
    if s >= 129: return p in end
    if p >= max(end): return False
    moves = [g(s+1, p+1, end), g(s*2, p+1, end)]
    if (p + 1) % 2 == (end[0] % 2):
        if any(moves):
            return True
    if (p + 1) % 2 != (end[0] % 2):
        if all(moves):
            return True

print([s for s in range(1, 129) if g(s, 0, [2]) ])
print([s for s in range(1, 129) if g(s, 0, [3]) ])
print([s for s in range(1, 129) if g(s, 0, [2, 4]) and not (g(s, 0, [2]))])
