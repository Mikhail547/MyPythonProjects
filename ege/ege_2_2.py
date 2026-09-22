for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((((not y) or x) == ((not x) or w)) and (z or x)):
                    print(y, w, x, z)

# (((not y) or x) == ((not x) or w)) and (z or x)