h1 = int(input()) 
m1 = int(input()) - 1
h2 = int(input()) 
m2 = int(input())
zero = '0'
min_in_h1_and_m1 = h1 * 60 + m1
min_in_h2_and_m2 = h2 * 60 + m2
while min_in_h1_and_m1 < min_in_h2_and_m2:
    min_in_h1_and_m1 += 1
    h1 = min_in_h1_and_m1 // 60
    m1 = min_in_h1_and_m1 % 60
    if 0 <= h1 < 10:
        h1 = '0' + str(h1)
    if 0 <= m1 < 10:
        m1 = '0' + str(m1)       
    print(h1,m1, sep=':')
