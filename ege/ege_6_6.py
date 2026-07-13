import turtle as t
t.screensize(1000,1000)
t.tracer(0)
k = 30
t.left(90)
t.dot(10)
t.down()
for i in range(2):
    t.forward(3*k)
    t.left(90)
    t.backward(10*k)
    t.left(90)
t.up()
t.backward(10*k)
t.right(90)
t.forward(8*k)
t.left(90)
t.down()
for i in range(2):
    t.forward(16*k)
    t.right(90)
    t.forward(8*k)
    t.right(90)
t.up()
for x in range(-100,100):
    for y in range(-100,100):
        t.goto(x*k,y*k)
        t.dot(5)


t.update()
t.done()
