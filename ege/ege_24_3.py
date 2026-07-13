with open('24_27777 (1).txt') as f:
    s = f.read()
v = '0123456789AB'
max_len = 0
n_len = 0
for a in s:
    if a in v:
        n_len += 1
        max_len = max(n_len, max_len)
    else:
        n_len = 0
print(max_len)