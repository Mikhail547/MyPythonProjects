import turtle as t
t.screensize(10000,8000)
t.tracer(0)
t.dot(5)
k = 20
t.down()
for i in range(7):
    t.right(45)
    t.forward(11*k)
    t.right(45)
t.up()
for x in range(-20,20):
    for y in range(-20,20):
        t.goto(x*k,y*k)
        t.dot(5)
t.update()
t.done()
