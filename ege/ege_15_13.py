for a in range(2000* 500):
    if all((x*y < a) or (5*x < y) or (486 <= x) for x in range(486) for y in range(2500)):
        print(a)
        break