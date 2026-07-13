import turtle as t
t.screensize(5000, 3000)
t.tracer(0)
t.dot(5)
k =15
t.left(90)
t.right(315)
t.down()
for _ in range(7):
    t.forward(12 * k)
    t.right(45)
    t.forward(6*k)
    t.right(135)
t.up()
for x in range(-100,100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(2)
t.done()
t.update()


