import turtle as t
t.screensize (3000, 1000)
k = 13
t.tracer(0)
t.dot(9)
t.left(90)


for i in range(6):
    t.forward(33 * k)
    t.right(90)
    t.forward(20 * k)
    t.right(90)
t.up()
t.forward(3 * k)
t.right(90)
t.forward(9 * k)
t.left(90)
t.down()
for i in range(6):
    t.forward(24 * k)
    t.right(90)
    t.forward(25 * k)
    t.right(90)
t.up()
for x in range(- 50, 50):
    for y in range(- 50, 50):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()
print(12*24)