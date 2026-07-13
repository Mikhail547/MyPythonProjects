for x1 in range(-100,100):
    for x2 in range(-100,100):
        for x3 in range(-100,100):
            for x4 in range(-100,100):
                if (3*x1 + 2*x2 -3*x3 + 5*x4 == 10 and
                    2*x1 - x2 + 5*x3 - x4 == 5 and x1 + x2 - 3*x3 + 2*x4 == 2 and
                    2*x1 + 2*x2 - x3 - x4 == -1):
                    print(f'x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}', sep='\n')
                    



