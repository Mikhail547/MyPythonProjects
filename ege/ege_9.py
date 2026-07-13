import turtle as t
t.screensize(1000, 1000)
t.tracer(0)
t.dot(5)
k = 15
t.down()
for _ in range(5):
    t.forward(29*k)
    t.right(90)
    t.forward(27*k)
    t.right(90)
t.up()
t.forward(3*k)
t.right(90)
t.forward(9*k)
t.left(90)
t.down()
for _ in range(5):
    t.forward(72*k)
    t.right(90)
    t.forward(95*k)
    t.right(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)

print(19*27)