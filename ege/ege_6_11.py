import turtle as t
t.screensize(3000, 5000)
t.tracer(0)
t.left(90)
t.dot(5)
k = 15
t.down()

for _ in range(3):
    t.forward(32*k)
    t.right(90)
    t.forward(38*k)
    t.right(90)
t.up()
t.forward(25*k)
t.right(90)
t.forward(21*k)
t.left(90)
t.down()
for _ in range(3):
    t.forward(29*k)
    t.right(90)
    t.back(18*k)
    t.right(90)
t.up()


for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()
# 1705

