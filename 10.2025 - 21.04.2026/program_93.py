w = input()
flag = False
for i in range(0, len(w)):
    for j in range(10):
        if str(j) in w[i]:
            flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')
