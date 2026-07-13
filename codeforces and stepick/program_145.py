s = list(range(ord('a'), ord('z')+1))
sl = list(chr(i) for i in s)
for i in range(1, len(sl)):
    sl[i] = sl[i][0]*(i+1)
print(sl)
