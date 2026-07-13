x1 = int(input()) 
a1 = x1 // 100
a2 = x1 % 100 // 10
a3 = x1 % 100 % 10
a4 = x1 - max(a1, a2, a3) - min(a1, a2, a3)
if a4 == max(a1, a2, a3) - min(a1, a2, a3):
    print('число интересное')
else:
    print('число неинтересное')
