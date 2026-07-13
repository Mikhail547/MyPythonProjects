name = input()
counter = -1
while name != 'Левон':
    if name == 'Александра':
        while name != 'Левон':
            counter += 1
            name = input()
    else:
        name = input()
print(counter)
