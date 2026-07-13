n = int(input())
b = 0
for i in range(0, 23 + 1):
    b = i ** n 
    if i < 24 and b < 59:
        if i < 10:
            i = '0' +str(i)
        if b < 10:
            b ='0'+ str(b) 
            
        print(i, b, sep=':')
