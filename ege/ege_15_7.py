def f(a):
    return all(( ((x&114) != 0) or ((x&94) != 0)) <= (((x&73) == 0) <= ((x&a) != 0)) for x in range(1, 1000))

for a in range(1, 1000): # с 1 для натуральных А
    if f(a):
        print(a) # Выводит 150
        break
