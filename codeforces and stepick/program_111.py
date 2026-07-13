s = input()
counter = 0
for i in range(10):        
    counter += s.count(str(i))
print(counter)
