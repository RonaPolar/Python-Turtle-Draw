import turtle
polar = turtle.Turtle()
polar.pensize(3)
polar.speed(10)
polar.hideturtle()
  
r = 10 #radius for circle
  
for i in range(100): # loop for spiral circle
    polar.circle(r + i, 50)

turtle.done()