import turtle
polar = turtle.Turtle()
polar.pensize(3)
polar.speed(10)
polar.hideturtle()

r = 10 #radius for smallest circle
n = 10 #number of circles to draw
  
for i in range(1, n + 1, 1): # loop for tangent circles
    polar.circle(r * i)

turtle.done()