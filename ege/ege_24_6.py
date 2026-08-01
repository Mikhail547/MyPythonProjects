with open('24_29354.txt') as f:
    s = f.readline().split('BC')
    m = 0
    for i in range(len(s)):
        s[i] = len(s[i]) + 2
    s[0] -= 1
    s[1] -= 1
    for i in range(len(s)-190):
        l = sum(a for a in s[i:i+191])
        m = max(m, l)


print(m)

