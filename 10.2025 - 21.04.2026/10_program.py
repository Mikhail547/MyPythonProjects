a = int(input())
b = int(input())
c = int(input())
x = int(input())
if a < b:
    b = a
if b < a:
    a = b
if x < c:
    c = x
if c < x:
    x = c
if b >= x:
    print(x)
if x > b:
    print(b)
