import turtle as t
t.screensize(1000,1000)
t.tracer(0)
t.dot(5)
k = 15
t.left(90)
t.down()
for i in range(2):
    t.forward(1*k)
    t.left(270)
    t.forward(16*k)
    t.right(90)
t.up()
t.backward(4*k)
t.right(90)
t.forward(10*k)
t.left(90)
t.down()
for i in range(2):
    t.forward(17*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)
t.up()
for x in range(100):
    for y in range(-20,100):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()
