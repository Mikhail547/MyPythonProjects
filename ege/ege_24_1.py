with open ('DEMO_24.txt') as f:
    s = f.readline().split ('Y') 
    m = 0
    for i in range(len(s) - 80):
        k = sum(str(a).count('2025') for a in s[i:i +81])
        if k >= 90:
            y = sum(len(a) for a in s[i:i +81])
            m = max(m, y + 80)
print(m)