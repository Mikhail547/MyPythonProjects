for a in range(1, 10000):
    if  all(((x % a == 0) or ((70 <= x <= 90) <= (x % 22 > 0))) == True for x in range(1, 10000)):
        print(a)
