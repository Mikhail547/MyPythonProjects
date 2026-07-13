import turtle as t
t.screensize(9000, 600)
t.tracer(0)
t.dot(9)
k = 15
t.down()
t.shape("turtle")

t.left(90)
t.backward(20*k)
for i in range(8):
    t.forward(16*k)
    t.right(90)
    t.forward(22*k)
    t.right(90)
t.up()
t.forward(5*k)
t.right(90)
t.forward(5*k)
t.left(90)
t.down()
for j in range(8):
    t.forward(52*k)
    t.right(90)
    t.forward(77*k)
    t.right(90)
t.up()
for x in range(-50,100):
    for y in range(-50,50):
        t.goto(x*k,y*k)
        t.dot(5)
t.update()
t.done()
