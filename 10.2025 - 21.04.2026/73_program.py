from turtle import *
tracer(0)
pendown()
k = 10
left(90)
counter = 0
begin_fill()
for i in range(6):
    forward(2 * k)
    right(120)
    for j in range(2):
        right(330)
        forward(4 * k)
end_fill()
penup()
canvas = getcanvas()
for x in range(-30 , 30):
    for y in range(-30 , 30 ):
        if canvas.find_overlapping(x * k, y* k, x * k, y * k) == (5,):
            counter += 1
print(counter)
done()