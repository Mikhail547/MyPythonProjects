money = int(input())
counter = 0
while money != 0:
   if money - 25 >= 0:
      counter += 1
      money -= 25
   elif money - 10 >= 0:
      counter += 1
      money -= 10
   elif money - 5 >= 0:
      counter += 1
      money -= 5
   elif money - 1 >= 0:
      counter += 1
      money -= 1
print(counter)
