import turtle as t
t.screensize(5000,5000)
t.tracer(0)
t.dot(1)
k=15
t.left(90)
for i in range(2):
    t.forward(14*k)
    t.left(270)
    t.backward(12*k)
    t.right(90)
t.done()