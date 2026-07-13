import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.dot(9)
k = 15
t.down()
t.shape("turtle")

for i in range(10):
    t.forward(5 * k)
    t.right(90)
    t.forward(3 * k)
    t.right(90)
    t.forward(2 * k)
t.up()
for x in range(- 50, 50):
    for y in range(-50, 50):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()