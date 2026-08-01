import fnmatch

start = (89000000 // 9874) * 9874
for x in range(start, 10 ** 10 + 1, 9874):
    s = str(x)
    if fnmatch.fnmatch(s, '89*6?7?9?'):
        print(x, x // 9874)
