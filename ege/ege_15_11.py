for a in range(100, 0, -1):
    if all((x > a) or (y > a) or (x + 2*y < 80) for x in range(200) for y in range(200)):
        print(a)
        break
