numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.insert(100, 4)
numbers.insert(100, 5)
numbers.insert(100, 6)

del numbers[0]

numbers *= 2
numbers.insert(3, 25)
print(numbers)
