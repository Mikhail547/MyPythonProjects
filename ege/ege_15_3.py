max_pr = 0
for x in range(1, 486):
    for y in range(1, 2426):
        if ((5 * x < y) or (486 <= x)) == False:
            if max_pr < x * y:
                max_pr = x * y
print(max_pr+1)

