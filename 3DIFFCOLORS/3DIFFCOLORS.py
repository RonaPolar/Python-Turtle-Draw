import turtle
t = turtle.Turtle()
t.speed(5)
t.hideturtle()
t.penup()
t.fillcolor('HotPink')
t.begin_fill()
t.backward(120)
t.circle(50)
t.end_fill()
t.fillcolor('Red')
t.begin_fill()
t.forward(55)
for i in range(3):
    t.forward(115)
    t.left(120)
t.end_fill()
t.fillcolor('SeaGreen')
t.begin_fill()
t.forward(135)
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()