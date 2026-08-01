import turtle as t
t.tracer(0)
t.screensize(3000, 4000)
t.dot(5)
k = 15
t.left(90)
t.down()
for _ in range(7):
    t.forward(12*k)
    t.right(90)
    t.forward(20*k)
    t.right(90)
t.up()
t.forward(1*k)
t.right(90)
t.forward(10*k)
t.left(90)
t.down()
for _ in range(7):
    t.forward(66*k)
    t.right(90)
    t.forward(92*k)
    t.right(90)
t.up()

for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)
t.update()
t.done()
print(11*10)
