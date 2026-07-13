import turtle as t
t.screensize(10000,8000)
t.tracer(0)
k = 15
t.left(90)
t.dot(9)
t.down()
for i in range(3):
    t.forward(20*k)
    t.right(90)
    t.forward(4*k)
    t.right(90)
for i in range(3):
    t.forward(6*k)
    t.right(90)
    t.forward(13*k)
    t.right(90)
t.up()
for x in range(-100,100):
    for y in range(-100,100):
        t.goto(x*k,y*k)
        t.dot(5)
t.done()
t.update()