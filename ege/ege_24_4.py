with open('33.txt') as f:

    s = f.readline().split('BC')
    m = 0
    for i in range(len(s)):
        s[i] = len(s[i]) + 2
    s[0] -= 1
    s[-1] -= 1
    for i in range(len(s) - 180):
        m = max(m, sum(s[i:i + 181]))
print(m)




