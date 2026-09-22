import turtle as t
t.screensize(3000, 5000)
t.tracer(0)
t.left(90)
t.dot(5)
k = 15
t.down()

for _ in range(7):
    t.forward(23*k)
    t.left(270)
    t.forward(27*k)
    t.right(90)
t.up()
t.forward(1*k)
t.right(90)
t.forward(7*k)
t.left(90)
t.down()

for _ in range(7):
    t.forward(96*k)
    t.right(90)
    t.forward(93*k)
    t.right(90)
t.up()

for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()
# 7 896000 bit
