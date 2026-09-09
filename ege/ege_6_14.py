import turtle as t
t.screensize(3000, 5000)
t.tracer(0)
t.left(90)
t.dot(5)
t.down()
k = 15

for _ in range(6):
    t.forward(24*k)
    t.right(90)
    t.forward(30*k)
    t.right(90)
t.up()
t.forward(2*k)
t.right(90)
t.forward(10*k)
t.left(90)
t.down()

for _ in range(6):
    t.forward(75*k)
    t.right(90)
    t.forward(71*k)
    t.right(90)

t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()