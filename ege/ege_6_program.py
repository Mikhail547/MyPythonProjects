import turtle as t
t.screensize (2000, 1000)
t.tracer(0)
k = 15
t.dot(9)
t.left(90)
for i in range(2):
    t.forward(14*k)
    t.left(270)
    t.backward(12*k)
    t.right(90)
t.up()
t.forward(9*k)
t.right(90)
t.backward(7*k)
t.left(90)
t.down
for i in range(2):
    t.forward(13*k)
    t.right(90)
    t.backward(6*k)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range(-50):
        t.goto(x*k, y*k)
        t.dot(5)
    
t.update()
t.done()