import turtle as t
t.tracer(0)
t.screensize(3000,5000)
k = 15
t.dot(5)
t.right(90)
t.down()
t.right(45)
for _ in range(3):
    t.right(45)
    t.forward(10*k)
    t.right(45)
t.right(315)
t.forward(10*k)
t.right(90)
t.forward(20*k)
t.right(90)
for _ in range(2):
    t.forward(10*k)
    t.right(90)

t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x*k, y*k)
        t.dot(5)


t.update()
t.done()
print(9*19 + 9*10)
