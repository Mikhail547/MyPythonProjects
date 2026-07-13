import turtle as t
t.screensize (120000, 100000)
k = 15
t.tracer(0)
t.dot(5)
t.down()
t.left(90)
for i in range(7):
    t.forward(158*k)
    t.right(90)
    t.forward(23*k)
    t.right(90)
t.up()
t.forward(3*k)
t.right(90)
t.forward(5*k)
t.right(90)
t.down()
for i in range(7):
    t.forward(252*k)
    t.right(90)
    t.forward(398*k)
    t.right(90)
t.up()
for x in range(-40, 500):
    for y in range(-20,500):
        t.goto(x*k, y*k)
        t.dot(5)
t.done()
t.update()

