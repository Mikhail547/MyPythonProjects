import turtle as t
t.screensize(5000, 8000)
t.tracer(0)
k = 16
t.left(90)
t.down()
t.dot(5)
for _ in range(6):
    t.forward(71*k)
    t.right(90)
    t.forward(73*k)
    t.right(90)
t.up()
t.forward(18*k)
t.right(90)
t.forward(22*k)
t.left(90)
t.down()
for _ in range(6):
    t.forward(45*k)
    t.right(90)
    t.forward(58*k)
    t.right(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(4)


t.update()
t.done()