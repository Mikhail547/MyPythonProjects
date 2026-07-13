for w in range(0, 1):
  for x in range(0, 1):
    for y in range(0, 1):
      for z in range(0, 1):
        if not(w <= (x == y)) * (z <= x) == 1:
          print(w, x, y, x)