from turtle import *
tracer(0)
k = 10
left(90)
pendown()
begin_fill()
for i in range(1, 2 + 1):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
for j in range(1, 1):
    forward(5 * k)
    right(90)
    forward(14 *  k)
    left(90)
for a in range(1, 4 + 1):
    forward(17 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
end_fill()


done()