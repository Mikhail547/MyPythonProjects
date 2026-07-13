n  = int(input())
m = int(input())
counter = 0
for i in range(1, n):
    for j in range(1, n):
        for z in range(1, n):
            if i * 3 + j + 2 * z == m:
                counter += 1  
                print(j,' + 3×',  i, ' + 2×', z,' = ', m, sep='')
if counter == 0:
    print('При заданных n и m решений не существует.')