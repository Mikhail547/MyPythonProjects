import turtle as t
t.screensize(500, 500)
t.tracer(0)
t.dot(9)
k = 3
t.left(90)
t.down()
for i in range(6):
    t.forward(71*k)
    t.right(90)
    t.forward(73*k)
    t.right(90)
t.up()
t.forward(18*k)
t.right(90)
t.forward(22*k)
t.left(90)
t.down()
for i in range(6):
    t.forward(45*k)
    t.right(90)
    t.forward(58*k)
    t.right(90)

for x in range(-100, 100):
    for y in range(-100, 100):


t.update()
t.done()