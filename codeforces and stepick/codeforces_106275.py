a = int(input()) # катя
b = int(input()) # ваня
for x in range(b//4, a//4, -1):
    c = (a-1)//4+1 # купе кати
    d = x - (b-x*4-1) //2 # купе макса
    if c == d:
        print(x)
        break