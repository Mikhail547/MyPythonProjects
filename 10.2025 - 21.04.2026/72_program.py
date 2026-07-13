from turtle import *
tracer(0)
left(90)
q = 20
count = 0
begin_fill()
pendown()
for i in range(2):
    forward(13 * q)
    right(90)
    forward(18 * q)
    right(90)
penup()
end_fill()
begin_fill()
for j in range(1, 1):
    forward(5 * q)
    right(90)
    forward(9 * q)
    left(90)
pendown()
for k in range(2):
    forward(11 * q)
    right(90)
    forward(7 * q)
    right(90)
    end_fill()

canvas = getcanvas()
for x in range(-200 , 200):
    for y in range(-200 , 200 ):
        if canvas.find_overlapping(x * q, y* q, x * q, y * q) == (5,4):
            count += 1
print(count)
done()
