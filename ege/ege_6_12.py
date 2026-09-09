import turtle as t
t.screensize(3000, 5000)
t.tracer(0)
t.dot(5)
k = 15
t.left(90)
t.down()

for _ in range(2):
    t.forward(21*k)
    t.right(90)
    t.forward(27*k)
    t.right(90)
t.up()
t.forward(9*k)
t.right(90)
t.forward(10*k)
t.left(90)
t.down()
for _ in range(2):
    t.forward(86*k)
    t.right(90)
    t.forward(47*k)
    t.right(90)
t.up()

for x in range(-100, 100):
    for y  in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(4)
t.update()
t.done()

